from rest_framework import generics
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

from .models import EmployeeProfile
from .serializers import EmployeeProfileSerializer

User = get_user_model()


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
        print(employee)

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

        # get the user object
        user = User.objects.get(email=user)
        # update the user model with the new data
        user.first_name = request.data['first_name']
        user.last_name = request.data['last_name']
        user.email = request.data['email']
        user.save()
        data = request.data.copy()
        data.pop('first_name')
        data.pop('last_name')
        data.pop('email')
        resume = request.data.get('resume')
        if not resume:
            data.pop('resume')

        profile_picture = request.data.get('profile_picture')
        if not profile_picture:
            data.pop('profile_picture')

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
