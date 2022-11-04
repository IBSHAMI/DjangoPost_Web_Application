from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from django.conf import settings

# import token model from drf
from rest_framework.authtoken.models import Token

from .models import User, EmployeeProfile
from .serializers import (
    EmployeeProfileSerializer,
)


class EmployeeDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

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

        # pop out the user model from the response
        data = serializer.data
        user = data.pop('user')

        # add the first, last name and email to the response
        data["first_name"] = user['first_name']
        data["last_name"] = user['last_name']
        data["email"] = user['email']

        return Response(data)

    def update(self, request, *args, **kwargs):
        # get request data
        request = self.request
        user = request.user
        print(request.data)

        # get the user object
        user = User.objects.get(email=user)
        # update the user model with the new data
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.save()

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
























# # Create a generic view for the resume and profile picture
# class EmployeeResumeAPIView(APIView):
#     parser_classes = [FileUploadParser]
#
#     def put(self, request, *args, **kwargs):
#         # get the user
#         request = self.request
#         token = request.headers.get('Authorization').split(' ')[1]
#         user_email = Token.objects.get(key=token).user
#         user = User.objects.get(email=user_email)
#         employee = EmployeeProfile.objects.get(user=user)
#         # print(employee)
#         #
#         # # get the resume file from the request
#         # print(args)
#         # print(kwargs)
#         resume_serializer = ProfileResumeSerializer(data=request.data)
#         print(resume_serializer.is_valid())
#         # print(resume_serializer.is_valid())
#         # print(resume_serializer.data['file'])
#
#         if resume_serializer.is_valid(raise_exception=True):
#             resume_serializer.save()
#             return Response(status=201)
#         else:
#             return Response(status=400)
#
# # # Create views to handle resume and profile picture uploads
# # class EmployeeResumeAPIView(EmployeeDetailsAPIView):
# #     queryset = EmployeeProfile.objects.all()
# #     serializer_class = ProfileResumeSerializer
# #     parser_classes = [FileUploadParser]
# #
# #     # get object method is inherited from EmployeeDetailsAPIView
# #
# #     # Override the retrieve method to return only the file name
# #     def retrieve(self, request, *args, **kwargs):
# #         instance = self.get_object()
# #
# #         # get the file name of the resume and profile picture if they exist or empty string if they don't
# #         resume = instance.get_resume_filename()
# #
# #         # update instance with the file name of the resume and profile picture
# #         instance.resume = resume
#
#         serializer = self.get_serializer(instance)
#
#         return Response(serializer.data)
#
#     def update(self, request, *args, **kwargs):
#         print(request.data)
#         # get request data
#         request = self.request
#         user = request.user
#
#         # get the user object
#         user = User.objects.get(email=user)
#
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer, user)
#
#         return Response(serializer.data)
#
#     # Override the perform_update method to save the resume file alone
#     def perform_update(self, serializer, user):
#         employee = EmployeeProfile.objects.get(user=user)
#         print(serializer)
#         print(serializer.validated_data)
#
#         # check if new resume or profile picture is uploaded
#         resume = serializer.validated_data.get('resume')
#         print(resume)
#
#         if resume is None:
#             # if no new resume is uploaded, use the old one
#             resume = employee.resume
#
#         print(resume)
#
#         # update the employee profile
#         serializer.save(resume=resume)
