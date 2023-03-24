from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Job
from .choices_fields_data_job import (
    JOB_TYPE_CHOICES,
    JOB_LANGUAGE_CHOICES,
    JOB_EXPERIENCE_CHOICES,
    JOB_LOCATION_CHOICES,
)


# Create a Serializer class for job create
class JobCreateSerializer(serializers.ModelSerializer):
    # Add choices fields
    type = serializers.MultipleChoiceField(choices=JOB_TYPE_CHOICES)
    language = serializers.MultipleChoiceField(choices=JOB_LANGUAGE_CHOICES)
    experience = serializers.MultipleChoiceField(choices=JOB_EXPERIENCE_CHOICES)
    location = serializers.MultipleChoiceField(choices=JOB_LOCATION_CHOICES)

    class Meta:
        model = Job
        fields = [
            'pk',
            'title',
            'company_description',
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
    user = serializers.SerializerMethodField(read_only=True)
    update_url = serializers.SerializerMethodField(read_only=True)
    delete_url = serializers.SerializerMethodField(read_only=True)

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
        return {
            'company_name': obj.user.company_profile.company_name,
            'company_logo': obj.user.company_profile.company_logo,
            'company_location': obj.user.company_profile.company_location,
            'company_website': obj.user.company_profile.company_website,
            'company_size': obj.user.company_profile.company_size,
        }
