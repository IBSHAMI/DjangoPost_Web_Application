from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Job
from company.models import CompanyProfile
from .choices_fields_data_job import (
    JOB_TYPE_CHOICES,
    JOB_LANGUAGE_CHOICES,
    JOB_EXPERIENCE_CHOICES,
    JOB_LOCATION_CHOICES,
)


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
            'user'
        ]


# Create a Serializer class for job list
class JobListSerializer(serializers.ModelSerializer):
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
            'company_data',
        ]

    def get_company_data(self, obj):
        company_profile = CompanyProfile.objects.get(user=obj.user)
        print(obj.type)
        print(obj.language)
        return {
            'company_name': company_profile.company_name,
            'company_location': company_profile.company_location,
            'company_website': company_profile.company_website,
            'company_size': company_profile.company_size,
        }
