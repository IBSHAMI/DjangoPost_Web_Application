from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.generics import (
    GenericAPIView,
)
from rest_framework.response import Response

from ..models import Job
from company.models import CompanyProfile
from ..choices_fields_data_job import (
    JOB_TYPE_CHOICES,
    JOB_LANGUAGE_CHOICES,
    JOB_EXPERIENCE_CHOICES,
    JOB_LOCATION_CHOICES,
    JOB_SALARY_CHOICES,
    FRAMEWORK_CHOICES,
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
            'framework_choices': get_choices_name(FRAMEWORK_CHOICES),
        }
        return Response(content)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_total_jobs_and_framework_choices(request):
    total_jobs = Job.objects.filter(is_active=True).count()
    framework_choices = get_choices_name(FRAMEWORK_CHOICES)

    data = {
        'total_jobs': total_jobs,
        'framework_choices': framework_choices
    }

    return Response(data)


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
        return Response("Status changed successfully")
    else:
        raise serializers.ValidationError('You are not the owner of this job')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_job_title(request):
    job_id = request.GET.get('job_id')
    job_title = Job.objects.get(id=job_id).title

    return Response({'job_title': job_title})
