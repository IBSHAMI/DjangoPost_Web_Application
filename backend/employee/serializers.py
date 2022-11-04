from rest_framework import serializers

from backend.users.serializers import UserSerializer
from .models import EmployeeProfile


class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EmployeeProfile
        fields = [
            'user',
            'software_field',
            'expected_salary',
            'linkedin_url',
            'portfolio_url',
            'about',
            'resume',
            'profile_picture',
        ]
