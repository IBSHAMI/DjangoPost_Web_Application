from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework import status
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

from .models import Job, SavedJob, AppliedJob
from company.models import CompanyProfile
from employee.models import EmployeeProfile
from .serializers import (
    JobListSerializer,
    JobCreateSerializer,
    CompanyJobListSerializer,
    JobDetailSerializer,
    SavedJobSerializer,
    AppliedJobSerializer,
    ApplicantsJobListSerializer,
    ApplicantsJobUpdateSerializer,
)
from .choices_fields_data_job import (
    JOB_TYPE_CHOICES,
    JOB_LANGUAGE_CHOICES,
    JOB_EXPERIENCE_CHOICES,
    JOB_LOCATION_CHOICES,
    JOB_SALARY_CHOICES,
    FRAMEWORK_CHOICES,
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
            'job_salary_choices': get_choices_name(JOB_SALARY_CHOICES),
            'framework_choices': get_choices_name(FRAMEWORK_CHOICES),
        }
        return Response(content)


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
        framework_choice = request.GET.get('framework_choice')
        qs = super().get_queryset()

        if user.is_authenticated:
            if table_variant == 'All Jobs':
                qs = qs.filter(is_active=True).exclude(company__user=user)

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
                qs = qs.filter(title__icontains=search_term)
                
            
            if framework_choice is not None:
                print(framework_choice)
                qs = qs.filter(framework__contains=framework_choice)
            
            return qs
                   
                
        else:
            qs = qs.filter(is_active=True)
            
            if search_term is not None:
                qs = qs.filter(title__icontains=search_term)
                
            
            if framework_choice is not None:
                print(framework_choice)
                qs = qs.filter(framework__contains=framework_choice)
            
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


# create job for a specific company
class JobCreateView(CreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobCreateSerializer
    lookup_field = 'pk'

    def create(self, request, *args, **kwargs):
        # get authenticated user
        user = self.request.user

        # get data from request
        data = request.data.copy()
        data['company'] = CompanyProfile.objects.get(user=user).pk

        serializer = self.get_serializer(data=data)

        # add user and company description to the serializer
        serializer.user = user

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class JobDetailView(RetrieveAPIView):
    queryset = Job.objects.filter(is_active=True)
    serializer_class = JobDetailSerializer
    permission_classes = [AllowAny]


class JobUpdateView(UpdateAPIView):
    serializer_class = CompanyJobListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # get authenticated user
        user = self.request.user

        queryset = Job.objects.filter(user=user)
        return queryset

    def perform_update(self, serializer):
        # get company profile
        company = CompanyProfile.objects.get(user=self.request.user)
        # check if job is under user
        if serializer.instance.company == company:
            super().perform_update(serializer)
        else:
            raise serializers.ValidationError('You are not the owner of this job')


class JobDeleteView(DestroyAPIView):
    serializer_class = CompanyJobListSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # get authenticated user
        company = CompanyProfile.objects.get(user=self.request.user)

        queryset = Job.objects.filter(company=company)
        return queryset

    def perform_destroy(self, instance):
        # get company profile
        company = CompanyProfile.objects.get(user=self.request.user)
        # check if job is under user
        if instance.company == company:
            super().perform_destroy(instance)
        else:
            raise serializers.ValidationError('You are not the owner of this job')


class SavedJobCreateView(CreateAPIView):
    queryset = SavedJob.objects.all()
    serializer_class = SavedJobSerializer

    def create(self, request, *args, **kwargs):
        # get job id
        job_id = request.data.get('job_id')

        # get authenticated user
        user = self.request.user

        # get the employee profile
        employee = EmployeeProfile.objects.get(user=user).pk
        job = Job.objects.get(pk=job_id).pk

        data = {}
        data['employee'] = employee
        data['job'] = job

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # the job list is updated to not return jobs that is posted by the user
    # however, this is a double check to make sure the user cannot save a job they posted
    def perform_create(self, serializer):
        # check if the job is under the company user
        if not serializer.validated_data['job'].internal and serializer.validated_data['job'].company.user == self.request.user:
            raise serializers.ValidationError('You cannot save a job you posted')
        
        serializer.save()


class SavedJobDeleteView(DestroyAPIView):
    serializer_class = SavedJobSerializer

    def get_queryset(self):
        # get authenticated user
        user = self.request.user

        queryset = SavedJob.objects.filter(employee__user=user)
        return queryset

    def get_object(self):
        job = Job.objects.get(pk=self.request.data.get('job_id'))
        employee = EmployeeProfile.objects.get(user=self.request.user)

        obj = SavedJob.objects.get(job=job, employee=employee)

        return obj


class AppliedJobCreateView(CreateAPIView):
    queryset = AppliedJob.objects.all()
    serializer_class = AppliedJobSerializer

    def create(self, request, *args, **kwargs):
        # get job id
        job_id = request.data.get('job_id')

        # get authenticated user
        user = self.request.user

        # get the employee profile
        employee = EmployeeProfile.objects.get(user=user).pk
        job = Job.objects.get(pk=job_id)

        if job.is_active == False or job.internal:
            raise serializers.ValidationError('This job is not available')

        data = {}
        data['employee'] = employee
        data['job'] = job.pk

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    
    # the job list is updated to not return jobs that is posted by the user
    # however, this is a double check to make sure the user cannot apply a job they posted
    def perform_create(self, serializer):
        # check if the job is not under the user
        if serializer.validated_data['job'].company.user == self.request.user:
            raise serializers.ValidationError('You can not apply to your own job')
        
        serializer.save()
        

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
    

class ApplicantsUpdateView(UpdateAPIView):
    serializer_class = ApplicantsJobUpdateSerializer
    queryset = AppliedJob.objects.all()
    
     

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
        return Response(status=status.HTTP_200_OK)
    else:
        raise serializers.ValidationError('You are not the owner of this job')
