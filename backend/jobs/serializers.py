from rest_framework import serializers
from urllib.parse import urljoin
from django.conf import settings
from django.contrib.auth import get_user_model

from .models import Job, SavedJob, AppliedJob
from employee.models import EmployeeProfile

User = get_user_model()





# Create a Serializer class for job create
class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'pk',
            'title',
            'description',
            'location',
            'type',
            'framework',
            'language',
            'experience',
            'number_of_positions',
            'remote',
            'salary',
            'company',
        ]


# Create a Serializer class for job list
class JobListSerializer(serializers.ModelSerializer):
    company_name = serializers.SerializerMethodField(read_only=True)
    is_saved_job = serializers.SerializerMethodField(read_only=True)
    job_application_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'pk',
            'title',
            'type',
            'salary',
            'location',
            'experience',
            'language',
            'date_created',
            'number_of_positions',
            'internal',
            'company_name',
            'is_saved_job',
            'job_application_status',
        ]

    def get_company_name(self, obj):
        if obj.internal:
            return obj.job_company
        company = obj.company
        return company.company_name

    def get_is_saved_job(self, obj):
        user = self.context['request'].user

        if not user.is_authenticated:
            return False

        employee = EmployeeProfile.objects.get(user=user)
        job = obj

        if SavedJob.objects.filter(employee=employee, job=job).exists():
            return True

        return False

    def get_job_application_status(self, obj):
        request = self.context['request']

        if request.user.is_authenticated:
            employee = EmployeeProfile.objects.get(user=request.user)
            if AppliedJob.objects.filter(job=obj, employee=employee).exists():
                application = AppliedJob.objects.get(job=obj, employee=employee)
                print(application)
                print(application.application_status)
                return application.application_status

        return ""


# Create a Serializer class for job list for company
class CompanyJobListSerializer(serializers.ModelSerializer):
    number_of_applications = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'pk',
            'title',
            'type',
            'salary',
            'language',
            'date_created',
            'is_active',
            'number_of_applications',
        ]

    def get_number_of_applications(self, obj):
        job = obj
        number_of_applications = AppliedJob.objects.filter(job=job).exclude(application_status="rejected").count()
        return number_of_applications


class JobDetailSerializer(JobCreateSerializer):
    company_data = serializers.SerializerMethodField(read_only=True)
    is_applied = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'pk',
            'title',
            'description',
            'location',
            'type',
            'framework',
            'language',
            'experience',
            'number_of_positions',
            'date_created',
            'remote',
            'salary',
            'internal',
            'job_link',
            'company_data',
            'is_applied',
        ]

    def get_company_data(self, obj):
        if obj.internal:
            return {
                'company_name': obj.job_company,
                'company_location': None,
                'company_website': None,
                'company_size': None,
            }
        company = obj.company
        return {
            'company_name': company.company_name,
            'company_location': company.company_location,
            'company_website': company.company_website,
            'company_size': company.company_size,
            'company_logo': company.company_logo.url if company.company_logo else None,
        }

    def get_is_applied(self, obj):
        user = self.context['request'].user

        # if user is anonymous and not logged in
        if user.is_anonymous:
            return False

        # if user is logged in, check if he has applied for the job
        employee = EmployeeProfile.objects.get(user=user)
        job = obj

        if AppliedJob.objects.filter(employee=employee, job=job).exists():
            return True

        return False


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = [
            'employee',
            'job',
        ]


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = [
            'employee',
            'job',
        ]


class AppliedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedJob
        fields = [
            'employee',
            'job',
        ]


class ApplicantsJobListSerializer(serializers.ModelSerializer):
    employee_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AppliedJob
        fields = [
            'pk',
            'employee_data',
            'date_applied',
        ]

    def get_employee_data(self, obj):
        employee = obj.employee
        employee_data = {
            'pk': employee.pk,
            'first_name': employee.user.first_name,
            'last_name': employee.user.last_name,
            'email': employee.user.email,
            'experience': employee.experience,
            'expected_salary': employee.expected_salary,
            'linkedin_url': employee.linkedin_url,
            'portfolio_url': employee.portfolio_url,
        }

        return employee_data


class ApplicantsJobUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedJob
        fields = [
            'pk',
            'application_status',
        ]

    def update(self, instance, validated_data):
        request = self.context['request']
        update_message = request.data.get('update_message')
        if update_message == 'rejected':
            instance.application_status = 'rejected'
        elif update_message == 'resume downloaded':
            instance.application_status = 'resume_downloaded'
        instance.save()
        return instance
