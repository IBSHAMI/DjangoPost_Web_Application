from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


# Overwrite the custom user registration serializer
class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    # Added username and email fields to be used for registration
    # Since our custom user model uses email as the username field
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('id', 'username', 'email', 'password')
