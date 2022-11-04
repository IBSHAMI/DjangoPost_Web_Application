from abc import ABC

from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from .models import User, EmployeeProfile, CompanyProfile, PayPalAccount


# Overwrite the custom user registration serializer
class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    # Added username and email fields to be used for registration
    # Since our custom user model uses email as the username field
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'email', 'password')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


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


# # create a serializer for the resume and image fields
# class ProfileResumeSerializer(serializers.Serializer):
#     resume = serializers.FileField()
#
#     class Meta:
#         fields = [
#             'resume',
#         ]
#
#
# class ProfilePictureSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = EmployeeProfile
#         fields = ['profile_picture']
