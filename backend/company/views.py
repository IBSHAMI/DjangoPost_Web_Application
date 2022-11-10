from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

from .models import CompanyProfile
from .serializers import CompanyProfileSerializer

User = get_user_model()


class CompanyDetailsAPIView(generics.RetrieveUpdateAPIView):
    queryset = CompanyProfile.objects.all()
    serializer_class = CompanyProfileSerializer
    parser_classes = (MultiPartParser, FormParser, FileUploadParser)

    def get_object(self):
        # get the sent request
        request = self.request

        # get the user Token
        token = request.headers.get('Authorization').split(' ')[1]
        user_email = Token.objects.get(key=token).user
        user = User.objects.get(email=user_email)

        # get the company profile
        company = CompanyProfile.objects.get(user=user)

        get_object = company

        return get_object

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()

        # get the file name of the company logo if it exists or empty string if it doesn't
        company_logo = instance.get_company_logo_filename()

        # send the file name only to the frontend
        instance.company_logo = company_logo

        serializer = self.get_serializer(instance)

        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data.copy()
        # Check if company logo is being updated
        company_logo = request.data.get('company_logo')
        if not company_logo:
            data.pop('company_logo')

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)

# #  Create a view to recieve and send customer messages
# class EmployeeContactSupportAPIView(APIView):
#
#     def post(self, request, *args, **kwargs):
#         admin_email = 'admin@admin.com'
#
#         # get the sent request data
#         data = request.data
#
#         first_name = data['first_name']
#         last_name = data['last_name']
#         email = data['email']
#         message = data['message']
#
#         # send the message to the customer support email
#         send_mail(
#             subject=f'Customer Support request from {first_name} {last_name}',
#             message=message + f'customer email: {email}',
#             from_email=admin_email,
#             recipient_list=[admin_email],
#         )
#
#         return Response({'message': 'Message sent successfully'})
