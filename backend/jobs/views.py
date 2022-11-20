from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .models import Job
from .serializers import JobCreateSerializer, JobListSerializer
from company.models import CompanyProfile


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
        if table_variant == 'active':
            qs = qs.filter(is_active=True)
        elif table_variant == 'inactive':
            qs = qs.filter(is_active=False)
        return qs


# List all jobs for a specific company
class JobCreateView(CreateAPIView):
    serializer_class = JobCreateSerializer
    lookup_field = 'pk'

    def perform_create(self, serializer):
        # get authenticated user
        user = self.request.user

        # get company description
        company = get_object_or_404(CompanyProfile, user=user)
        company_description = company.company_description

        # create job
        serializer.save(user=user, company_description=company_description)


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
