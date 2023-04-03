from rest_framework import serializers
from rest_framework.generics import DestroyAPIView

from ..models import Job, SavedJob
from company.models import CompanyProfile
from employee.models import EmployeeProfile
from ..serializers import (
    CompanyJobListSerializer,
    SavedJobSerializer,
)


class JobDeleteView(DestroyAPIView):
    serializer_class = CompanyJobListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # get authenticated user
        company = CompanyProfile.objects.get(user=self.request.user)

        queryset = Job.objects.filter(company=company)
        return queryset

    def perform_destroy(self, instance):
        # get company profile
        company = CompanyProfile.objects.get(user=self.request.user)
        # check if job is under user
        if instance.company == company:
            super().perform_destroy(instance)
        else:
            raise serializers.ValidationError('You are not the owner of this job')


class SavedJobDeleteView(DestroyAPIView):
    serializer_class = SavedJobSerializer

    def get_queryset(self):
        # get authenticated user
        user = self.request.user

        queryset = SavedJob.objects.filter(employee__user=user)
        return queryset

    def get_object(self):
        job = Job.objects.get(pk=self.request.data.get('job_id'))
        employee = EmployeeProfile.objects.get(user=self.request.user)

        obj = SavedJob.objects.get(job=job, employee=employee)

        return obj
