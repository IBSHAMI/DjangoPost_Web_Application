from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .models import EmployeeProfile
from .choices_fields_data_employee import JOB_EXPERIENCE_CHOICES, JOB_SALARY_CHOICES
from .serializers import (
    EmployeeProfileSerializer,
    EmployeeProfilePictureSerializer,
    EmployeeProfileResumeSerializer
)

User = get_user_model()


def get_choices_name(choices):
    return [choice[1] for choice in choices]


# Create a view that send the choices fields data to the frontend
class EmployeeChoicesView(GenericAPIView):

    def get(self, request, *args, **kwargs):
        content = {
            'job_experience_choices': get_choices_name(JOB_EXPERIENCE_CHOICES),
            'job_salary_choices': get_choices_name(JOB_SALARY_CHOICES),
        }
        return Response(content)


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

        print(data)

        # update the employee profile data fields without profile picture or resume
        # because they are handled in a different view
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        # return only data without the user model for safety
        return Response(data)


class EmployeeProfilePictureAPIView(generics.RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfilePictureSerializer

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


class EmployeeProfileResumeAPIView(generics.RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileResumeSerializer

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
        serializer = self.get_serializer(instance)

        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_applicant_resume(request, pk):
    # get the applicant profile
    applicant = get_object_or_404(EmployeeProfile, pk=pk)

    resume = EmployeeProfileResumeSerializer(applicant, context={'request': request})

    # send the resume file to the frontend
    return Response(resume.data)


#  Create a view to recieve and send customer messages
class EmployeeContactSupportAPIView(APIView):

    def post(self, request, *args, **kwargs):
        admin_email = 'admin@admin.com'

        # get the sent request data
        data = request.data

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        message = data['message']

        # send the message to the customer support email
        send_mail(
            subject=f'Customer Support request from {first_name} {last_name}',
            message=message + f'customer email: {email}',
            from_email=admin_email,
            recipient_list=[admin_email],
        )

        return Response({'message': 'Message sent successfully'})
