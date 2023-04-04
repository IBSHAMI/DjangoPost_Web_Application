from rest_framework.permissions import AllowAny
from rest_framework import serializers
from rest_framework.generics import (
    GenericAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)

from ..models import Job, AppliedJob
from company.models import CompanyProfile
from ..serializers import (
    JobDetailSerializer,
    CompanyJobListSerializer,
    ApplicantsJobUpdateSerializer,
)


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True).select_related('company')
    serializer_class = JobDetailSerializer
    permission_classes = [AllowAny]


class JobUpdateView(UpdateAPIView):
    serializer_class = CompanyJobListSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Job.objects.filter(user=user)
        return queryset

    def perform_update(self, serializer):
        company = CompanyProfile.objects.get(user=self.request.user)
        if serializer.instance.company == company:
            super().perform_update(serializer)
        else:
            raise serializers.ValidationError('You are not the owner of this job')


class ApplicantsUpdateView(UpdateAPIView):
    serializer_class = ApplicantsJobUpdateSerializer
    queryset = AppliedJob.objects.all()
