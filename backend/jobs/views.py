from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .models import Job
from .serializers import JobSerializer, JobDetailSerializer


class JobListView(ListCreateAPIView):
    serializer_class = JobSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return Job.objects.filter(is_active=True)

    def perform_create(self, serializer):
        # get authenticated user
        user = self.request.user

        # create job
        serializer.save(user=user)


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobDetailSerializer
    lookup_field = 'pk'


class JobUpdateView(UpdateAPIView):
    serializer_class = JobSerializer
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
    serializer_class = JobSerializer
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
