from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.conf import settings

# import token model from drf
from rest_framework.authtoken.models import Token

from .models import User, EmployeeProfile, CompanyProfile, PayPalAccount
from .serializers import EmployeeProfileSerializer

# Get file locations in order to return only the file name to the frontend
media_file_location = settings.MEDIA_ROOT
resume_file_location = settings.MEDIA_ROOT + '/users/employee/resumes/'
profile_picture_file_location = settings.MEDIA_ROOT + '/users/employee/profile_pics/'


class EmployeeDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer

    def get_object(self):
        # get the sent request
        request = self.request

        # get the user Token
        token = request.headers.get('Authorization').split(' ')[1]  # get the token from the header
        user_email = Token.objects.get(key=token).user
        user = User.objects.get(email=user_email)

        # get the employee profile
        employee = EmployeeProfile.objects.get(user=user)

        get_object = employee

        return get_object

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # get the file name of the resume and profile picture if they exist or empty string if they don't
        resume = instance.get_resume_filename()
        profile_picture = instance.get_profile_picture_filename()

        # update instance with the file name of the resume and profile picture
        instance.resume = resume
        instance.profile_picture = profile_picture

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def perform_update(self, serializer):
        # get the user object
        user = self.request.user
        employee = EmployeeProfile.objects.get(user=user)

        # check if new resume or profile picture is uploaded
        resume = serializer.validated_data.get('resume')
        profile_picture = serializer.validated_data.get('profile_picture')

        if resume is None:
            # if no new resume is uploaded, use the old one
            resume = employee.resume
        if profile_picture is None:
            # if no new profile picture is uploaded, use the old one
            profile_picture = employee.profile_picture

        # update the employee profile
        serializer.save(resume=resume, profile_picture=profile_picture)
