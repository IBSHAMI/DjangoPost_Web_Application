from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .models import Job
from .serializers import JobSerializer


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

