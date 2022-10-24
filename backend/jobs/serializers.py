from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Job
from .validators import validate_title, unique_job_validator


class JobSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length=100, validators=[validate_title, unique_job_validator])
    user = serializers.SerializerMethodField()

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
            'internal',
            'user',
        ]

    def get_user(self, obj):
        return {
            'username': obj.user.username,
            'email': obj.user.email,
        }