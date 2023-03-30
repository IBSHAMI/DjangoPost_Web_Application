from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth import get_user_model

from .models import Job, SavedJob
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
        ]

    def get_company_name(self, obj):
        if obj.internal:
            return obj.job_company
        company = obj.company
        return company.company_name
    
    def get_is_saved_job(self, obj):
        user = self.context['request'].user
        employee = EmployeeProfile.objects.get(user=user)
        job = obj
        
        if SavedJob.objects.filter(employee=employee, job=job).exists():
            return True
        
        return False

    


# Create a Serializer class for job list for company
class CompanyJobListSerializer(serializers.ModelSerializer):
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
        ]


class JobDetailSerializer(JobCreateSerializer):
    company_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Job
        fields = [
            'pk',
            'title',
            'description',
            'location',
            'type',
            'language',
            'experience',
            'number_of_positions',
            'date_created',
            'remote',
            'salary',
            'internal',
            'job_link',
            'company_data',
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
        }


class SavedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedJob
        fields = [
            'employee', 
            'job',
        ]


