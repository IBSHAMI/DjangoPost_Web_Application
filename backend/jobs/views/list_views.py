from rest_framework.permissions import AllowAny
from rest_framework.generics import ListAPIView


from ..models import Job, SavedJob, AppliedJob
from company.models import CompanyProfile
from employee.models import EmployeeProfile
from ..serializers import (
    JobListSerializer,
    CompanyJobListSerializer,
    ApplicantsJobListSerializer,
)
from ..services.search_services import get_filtered_jobs, get_company_specific_filtered_jobs


# Create a view that get list of all jobs for main page
class JobListView(ListAPIView):
    queryset = Job.objects.select_related('company').all()
    serializer_class = JobListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        request = self.request
        user = request.user
        table_variant = request.GET.get('table_variant')
        search_term = request.GET.get('search_term')
        framework_choice = request.GET.get('framework_choice')
        qs = super().get_queryset()
        qs = get_filtered_jobs(qs, user, table_variant, search_term, framework_choice)
        return qs


# Create a class listAPIView to list all jobs
class CompanyJobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = CompanyJobListSerializer

    def get_queryset(self):
        # get request and extract table variant to filter queryset
        request = self.request
        search_term = request.GET.get('search_term')
        table_variant = request.GET.get('table_variant')
        company = CompanyProfile.objects.get(user=request.user)
        sorting_option = request.GET.get('sorting_option')
        qs = super().get_queryset()
        qs = qs.filter(company=company)
        qs = get_company_specific_filtered_jobs(qs, table_variant, sorting_option, search_term)
        return qs


class ApplicantsListView(ListAPIView):
    serializer_class = ApplicantsJobListSerializer

    def get_queryset(self):
        request = self.request
        job_id = request.GET.get('job_id')
        job = Job.objects.get(pk=job_id)
        applied_jobs = AppliedJob.objects.filter(job=job).select_related("employee").exclude(application_status='rejected')

        return applied_jobs
