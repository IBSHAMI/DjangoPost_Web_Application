from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    DestroyAPIView,
    UpdateAPIView,
)

from .models import Job
from .serializers import JobSerializer


class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'pk'

