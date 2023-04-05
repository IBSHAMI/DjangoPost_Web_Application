from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.conf import settings
import random
import string

from employee.models import EmployeeProfile
from company.models import CompanyProfile
from jobs.models import Job

User = settings.AUTH_USER_MODEL


# A view to handle creating demo users
# @api_view(['POST'])
# @permission_classes([AllowAny])
# def create_demo_user(request):
#     random_username =


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_if_profile_complete(request):
    user = request.user
    data = {}

    employee_profile = EmployeeProfile.objects.get(user=user)
    if any(field == '' or field is None for field in employee_profile.__dict__.values() if
           field != employee_profile.profile_picture):
        data['employee_profile_complete'] = False
    else:
        data['employee_profile_complete'] = True

    company = CompanyProfile.objects.get(user=user)
    if any(field == '' or field is None for field in company.__dict__.values() if field != company.company_logo):
        data['company_profile_complete'] = False
    else:
        data['company_profile_complete'] = True

    return Response(data)


@api_view(['GET'])
@permission_classes([AllowAny])
def get_webapp_status_data(request):
    data = {}
    # get number of jobs posted
    data["total_jobs"] = Job.objects.all().count()

    # get number of companies
    data["total_companies"] = CompanyProfile.objects.all().count()

    # get number of employees
    data["total_employees"] = EmployeeProfile.objects.all().count()

    return Response(data)
