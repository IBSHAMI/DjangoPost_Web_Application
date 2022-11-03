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
        fields = '__all__'

    # Since we using a nested serializer [user and employee models].
    # we have to override the update method to update the employee and user models alone
    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     first_name = validated_data['first_name']
    #     print("hereeee")
    #     print(first_name)
    #
    #     return instance
