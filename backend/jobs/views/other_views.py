from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response

from ..models import Job
from company.models import CompanyProfile
from ..serializers import (
    JobDetailSerializer,
    CompanyJobListSerializer,
)
from ..choices_fields_data_job import (
    JOB_TYPE_CHOICES,
    JOB_LANGUAGE_CHOICES,
    JOB_EXPERIENCE_CHOICES,
    JOB_LOCATION_CHOICES,
    JOB_SALARY_CHOICES,
)


def get_choices_name(choices):
    return [choice[1] for choice in choices]


# Create a view that send the choices fields data to the frontend
class JobChoicesView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        content = {
            'job_type_choices': get_choices_name(JOB_TYPE_CHOICES),
            'job_language_choices': get_choices_name(JOB_LANGUAGE_CHOICES),
            'job_experience_choices': get_choices_name(JOB_EXPERIENCE_CHOICES),
            'job_location_choices': get_choices_name(JOB_LOCATION_CHOICES),
            'job_salary_choices': get_choices_name(JOB_SALARY_CHOICES),
        }
        return Response(content)


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobDetailSerializer
    permission_classes = [AllowAny]


class JobUpdateView(UpdateAPIView):
    serializer_class = CompanyJobListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # get authenticated user
        user = self.request.user

        queryset = Job.objects.filter(user=user)
        return queryset

    def perform_update(self, serializer):
        # get company profile
        company = CompanyProfile.objects.get(user=self.request.user)
        # check if job is under user
        if serializer.instance.company == company:
            super().perform_update(serializer)
        else:
            raise serializers.ValidationError('You are not the owner of this job')


@api_view(['GET'])
@permission_classes([AllowAny])
def get_total_jobs(request):
    total_jobs = Job.objects.filter(is_active=True).count()
    return Response(total_jobs)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def change_job_status(request, pk):
    # get job
    job = get_object_or_404(Job, pk=pk)

    # get company profile
    company = CompanyProfile.objects.get(user=request.user)

    # check if job is under user
    if job.company == company:
        # update job status
        job.is_active = not job.is_active
        job.save()
        return Response(status=status.HTTP_200_OK)
    else:
        raise serializers.ValidationError('You are not the owner of this job')
