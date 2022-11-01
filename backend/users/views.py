from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# import token model from drf
from rest_framework.authtoken.models import Token

from .models import User, EmployeeProfile, CompanyProfile, PayPalAccount
from .serializers import EmployeeProfileSerializer


class EmployeeDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer

    def get_object(self):
        # get the sent request
        request = self.request

        # get the user Token
        token = request.headers.get('Authorization')
        user_email = Token.objects.get(key=token).user
        user = User.objects.get(email=user_email)

        # get the employee profile
        employee = EmployeeProfile.objects.get(user=user)

        get_object = employee

        return get_object

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
