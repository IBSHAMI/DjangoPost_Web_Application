from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Job
from .choices_fields_data import (
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
            'date_created',
            'remote',
            'salary',
            'user',
            'update_url',
            'delete_url',
        ]
        read_only_fields = ['date_created', 'user']

    def get_user(self, obj):
        return {
            'username': obj.user.username,
            'email': obj.user.email,
        }

    def get_update_url(self, obj):
        # Acess the request object from the serializer context
        request = self.context.get('request')
        if request is None:
            return None

        # get user from request
        user = request.user
        if obj.user == user:
            return reverse('api:jobs:job_update', kwargs={'pk': obj.pk}, request=request)
        else:
            return None

    def get_delete_url(self, obj):
        # Access the request object from the serializer context
        request = self.context.get('request')
        if request is None:
            return None

        # get user from request
        user = request.user
        if obj.user == user:
            return reverse('api:jobs:job_delete', kwargs={'pk': obj.pk}, request=request)
        else:
            return None
