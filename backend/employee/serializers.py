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
            # resume and profile picture are used to return
            # the file name of the resume and profile picture
            'resume',
            'profile_picture',
        ]


class EmployeeProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = [
            'profile_picture',
        ]

    def update(self, instance, validated_data):
        print('validated_data: ', validated_data)
        profile_picture = validated_data.get('profile_picture', None)
        if profile_picture is not None:
            instance.profile_picture = profile_picture
            instance.save()
        return instance


class EmployeeProfileResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = [
            'resume',
        ]
