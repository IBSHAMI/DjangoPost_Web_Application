from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework.response import Response

from ..models import Job, SavedJob, AppliedJob
from company.models import CompanyProfile
from employee.models import EmployeeProfile
from ..serializers import (
    JobCreateSerializer,
    SavedJobSerializer,
    AppliedJobSerializer,
)


# create job for a specific company
class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        # get authenticated user
        user = self.request.user

        # get data from request
        data = request.data.copy()
        data['company'] = CompanyProfile.objects.get(user=user).pk

        serializer = self.get_serializer(data=data)

        # add user and company description to the serializer
        serializer.user = user

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    
class SavedJobCreateView(CreateAPIView):
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer

    def create(self, request, *args, **kwargs):
        # get job id
        job_id = request.data.get('job_id')

        # get authenticated user
        user = self.request.user

        # get the employee profile
        employee = EmployeeProfile.objects.get(user=user).pk
        job = Job.objects.get(pk=job_id).pk

        data = {}
        data['employee'] = employee
        data['job'] = job

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # the job list is updated to not return jobs that is posted by the user
    # however, this is a double check to make sure the user cannot save a job they posted
    def perform_create(self, serializer):
        # check if the job is under the company user
        if serializer.validated_data['job'].company.user == self.request.user:
            raise serializers.ValidationError('You cannot save a job you posted')
        
        serializer.save()
        
        
class AppliedJobCreateView(CreateAPIView):
    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobSerializer

    def create(self, request, *args, **kwargs):
        # get job id
        job_id = request.data.get('job_id')

        # get authenticated user
        user = self.request.user

        # get the employee profile
        employee = EmployeeProfile.objects.get(user=user).pk
        job = Job.objects.get(pk=job_id)

        if job.is_active == False or job.internal:
            raise serializers.ValidationError('This job is not available')

        data = {}
        data['employee'] = employee
        data['job'] = job.pk

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    # the job list is updated to not return jobs that is posted by the user
    # however, this is a double check to make sure the user cannot apply a job they posted
    def perform_create(self, serializer):
        # check if the job is not under the user
        if serializer.validated_data['job'].company.user == self.request.user:
            raise serializers.ValidationError('You can not apply to your own job')
        
        serializer.save()
        