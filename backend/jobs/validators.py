from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Job


def validate_title(value):
    if len(value) < 10:
        raise serializers.ValidationError("Title is too short")
    return value


unique_job_validator = UniqueValidator(queryset=Job.objects.all(), message="Job with this title already exists")
