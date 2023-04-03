from rest_framework.response import Response
from rest_framework.permissions import  AllowAny
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
)

from ..models import Job, SavedJob, AppliedJob
from company.models import CompanyProfile
from employee.models import EmployeeProfile
from ..serializers import (
    JobListSerializer,
    CompanyJobListSerializer,
    ApplicantsJobListSerializer,
)







    
    
    
# Create a view that get list of all jobs for main page
class JobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        request = self.request
        user = request.user
        table_variant = request.GET.get('table_variant')
        search_term = request.GET.get('search_term')
        qs = super().get_queryset()

        if user.is_authenticated:
            print('user is authenticated')
            if table_variant == 'All Jobs':
                qs = qs.exclude(company__user=user)

            elif table_variant == 'Saved Jobs':
                employee = EmployeeProfile.objects.get(user=user)
                saved_jobs = SavedJob.objects.filter(employee=employee).select_related('job')

                saved_jobs_ids = [saved_job.job.id for saved_job in saved_jobs]
                
                qs = qs.filter(id__in=saved_jobs_ids)

            elif table_variant == 'Applied Jobs':
                employee = EmployeeProfile.objects.get(user=user)
                applied_jobs = AppliedJob.objects.filter(employee=employee).select_related('job')

                applied_jobs_ids = [applied_job.job.id for applied_job in applied_jobs]
                
                qs = qs.filter(id__in=applied_jobs_ids)
                
            if search_term is not None:
                qs = qs.filter(title__icontains=search_term, is_active=True)
                return qs
                
        else:
            qs = qs.filter(is_active=True)



        return qs
    
    
class CompanyJobListView(ListAPIView):
    queryset = Job.objects.all()
    serializer_class = CompanyJobListSerializer

    def get_queryset(self):
        # get request and extract table variant to filter queryset
        request = self.request
        search_term = request.GET.get('search_term')
        table_variant = request.GET.get('table_variant')
        company = CompanyProfile.objects.get(user=request.user)

        qs = super().get_queryset()
        qs = qs.filter(company=company)
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

        # filter queryset based on search term
        if search_term is not None:
            qs = qs.filter(title__icontains=search_term)

        return qs
    
    

class ApplicantsListView(ListAPIView):
    serializer_class = ApplicantsJobListSerializer

    def get_queryset(self):
        request = self.request
        # get job id
        job_id = request.GET.get('job_id')
        print(job_id)

        # get the job
        job = Job.objects.get(pk=job_id)
        
        # get the applied jobs
        applied_jobs = AppliedJob.objects.filter(job=job)
        
        return applied_jobs