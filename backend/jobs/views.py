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
        return Job.objects.all()

    def perform_create(self, serializer):
        # get authenticated user
        user = self.request.user

        # Return internal job True
        internal = True

        # create job
        serializer.save(user=user, internal=internal)

