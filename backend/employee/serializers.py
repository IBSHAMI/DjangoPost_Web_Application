from rest_framework import serializers

from users.serializers import UserSerializer
from .models import EmployeeProfile


class EmployeeProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = EmployeeProfile
        fields = [
            'user',
            'expected_salary',
            'linkedin_url',
            'portfolio_url',
            'experience',
            'about',
            'resume',
            'profile_picture',
        ]
