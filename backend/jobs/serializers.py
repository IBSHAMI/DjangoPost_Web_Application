from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Job
from company.models import CompanyProfile


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
    # create a company logo as an image field
    company_logo = serializers.SerializerMethodField(read_only=True)
    company_name = serializers.SerializerMethodField(read_only=True)

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
            'internal',
            'company_logo',
            'company_name',
        ]

    def get_company_logo(self, obj):
        if obj.internal:
            return None
        company_profile = CompanyProfile.objects.get(user=obj.user)
        return company_profile.company_logo.url

    def get_company_name(self, obj):
        if obj.internal:
            return obj.job_company
        company_profile = CompanyProfile.objects.get(user=obj.user)
        return company_profile.company_name


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
        company_profile = CompanyProfile.objects.get(user=obj.user)
        return {
            'company_name': company_profile.company_name,
            'company_location': company_profile.company_location,
            'company_website': company_profile.company_website,
            'company_size': company_profile.company_size,
        }
