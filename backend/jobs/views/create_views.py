from rest_framework import serializers
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
)
from rest_framework.response import Response

from ..models import Job, SavedJob, AppliedJob
from company.models import CompanyProfile
from ..serializers import (
    JobCreateSerializer,
    SavedJobSerializer,
    AppliedJobSerializer,
)
from ..services.create_services import (
    create_data_dictionary,
    check_if_user_can_apply,
    check_if_job_not_created_by_user,
)


# create job for a specific company
class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer

    def create(self, request, *args, **kwargs):
        user = self.request.user
        data = request.data.copy()
        data['company'] = CompanyProfile.objects.get(user=user).pk

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class SavedJobCreateView(CreateAPIView):
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer

    def create(self, request, *args, **kwargs):
        job_id = request.data.get('job_id')
        data, job = create_data_dictionary(self.request.user, job_id)

        if not check_if_job_not_created_by_user(job, self.request.user):
            raise serializers.ValidationError('You can not apply to your own job')

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class AppliedJobCreateView(CreateAPIView):
    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobSerializer

    def create(self, request, *args, **kwargs):
        job_id = request.data.get('job_id')
        data, job = create_data_dictionary(self.request.user, job_id)

        if not check_if_user_can_apply(job):
            raise serializers.ValidationError('This job is not available')

        if not check_if_job_not_created_by_user(job, self.request.user):
            raise serializers.ValidationError('You can not apply to your own job')

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

