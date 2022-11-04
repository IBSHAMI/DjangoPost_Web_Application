from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


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

