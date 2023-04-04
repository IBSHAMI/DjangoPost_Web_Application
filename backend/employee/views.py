from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .models import EmployeeProfile
from .choices_fields_data_employee import JOB_EXPERIENCE_CHOICES, JOB_SALARY_CHOICES
from .serializers import (
    EmployeeProfileSerializer,
    EmployeeProfilePictureSerializer,
    EmployeeProfileResumeSerializer,
    EmployeeProfileUpdateSerializer,
)
from .services import get_employee_profile

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
        request = self.request
        token = request.headers.get('Authorization').split(' ')[1]
        get_object, user = get_employee_profile(token)

        # check if the request is a PUT request
        if request.method == 'PUT':
            user.first_name = request.data.get('first_name', None)
            user.last_name = request.data.get('last_name', None)
            user.email = request.data.get('email', None)
            user.save()

        return get_object

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EmployeeProfileSerializer
        return EmployeeProfileUpdateSerializer

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


class EmployeeProfilePictureAPIView(generics.RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfilePictureSerializer

    def get_object(self):
        request = self.request
        token = request.headers.get('Authorization').split(' ')[1]
        get_object, _ = get_employee_profile(token)

        return get_object


class EmployeeProfileResumeAPIView(generics.RetrieveUpdateAPIView):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileResumeSerializer

    def get_object(self):
        request = self.requestn
        token = request.headers.get('Authorization').split(' ')[1]
        get_object, _ = get_employee_profile(token)
        return get_object

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def get_applicant_resume(request, pk):
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
