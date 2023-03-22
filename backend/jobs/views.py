from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .models import Job
from .serializers import JobCreateSerializer, JobListSerializer
from company.models import CompanyProfile
from .choices_fields_data_job import (
    JOB_TYPE_CHOICES,
    JOB_LANGUAGE_CHOICES,
    JOB_EXPERIENCE_CHOICES,
    JOB_LOCATION_CHOICES,
)

User = get_user_model()


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
        }
        return Response(content)


# Create a class listAPIView to list all jobs
class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer

    def get_queryset(self):
        # get request and extract table variant to filter queryset
        request = self.request
        table_variant = request.GET.get('table_variant')

        qs = super().get_queryset()
        qs = qs.filter(user=self.request.user)
        # filter queryset based on table variant
        if table_variant != 'all':
            if table_variant == 'active':
                qs = qs.filter(is_active=True)
            elif table_variant == 'inactive':
                qs = qs.filter(is_active=False)

        # order queryset by sorting option selected
        sorting_option = request.GET.get('sorting_option')
        if sorting_option != "None":
            if sorting_option == "Latest":
                qs = qs.order_by('-date_created')
            elif sorting_option == "Oldest":
                qs = qs.order_by('date_created')

        return qs


# create job for a specific company
class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        # get authenticated user
        user = self.request.user

        # get company description
        company = get_object_or_404(CompanyProfile, user=user)
        company_description = company.company_description

        # get data from request
        data = request.data.copy()
        data['user'] = User.objects.get(email=user).pk
        data['company_description'] = company_description

        serializer = self.get_serializer(data=data)

        # add user and company description to the serializer
        serializer.user = user
        serializer.company_description = company_description

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        from rest_framework import status
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobListSerializer
    lookup_field = 'pk'


class JobUpdateView(UpdateAPIView):
    serializer_class = JobListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # get authenticated user
        user = self.request.user

        queryset = Job.objects.filter(user=user)
        return queryset

    def perform_update(self, serializer):
        # check if job is under user
        if serializer.instance.user == self.request.user:
            super().perform_update(serializer)
        else:
            raise serializers.ValidationError('You are not the owner of this job')


class JobDeleteView(DestroyAPIView):
    serializer_class = JobListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # get authenticated user
        user = self.request.user

        queryset = Job.objects.filter(user=user)
        return queryset

    def perform_destroy(self, instance):
        # check if job is under user
        if instance.user == self.request.user:
            super().perform_destroy(instance)
        else:
            raise serializers.ValidationError('You are not the owner of this job')


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def change_job_status(request, pk):
    # get job
    job = get_object_or_404(Job, pk=pk)
    print(request.user)

    # check if job is under user
    if job.user == request.user:
        # update job status
        job.is_active = not job.is_active
        job.save()
        return Response(status=status.HTTP_200_OK)
    else:
        raise serializers.ValidationError('You are not the owner of this job')
