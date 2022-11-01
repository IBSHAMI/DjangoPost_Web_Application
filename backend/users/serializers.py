from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from .models import User, EmployeeProfile, CompanyProfile, PayPalAccount


# Overwrite the custom user registration serializer
class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    # Added username and email fields to be used for registration
    # Since our custom user model uses email as the username field
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'email', 'password')


class EmployeeProfileSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    resume = serializers.CharField()
    profile_picture = serializers.CharField()

    class Meta:
        model = EmployeeProfile
        fields = ('id',
                  'first_name',
                  'last_name',
                  'email',
                  'software_field',
                  'expected_salary',
                  'expected_salary_currency',
                  'linkedin_url',
                  'Portfolio_url',
                  'resume',
                  'profile_picture',
                  )
