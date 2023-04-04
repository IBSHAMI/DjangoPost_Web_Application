from rest_framework.authtoken.models import Token
from .models import EmployeeProfile
from users.models import User


def get_employee_profile(token):
    user_email = Token.objects.get(key=token).user
    user = User.objects.get(email=user_email)
    employee = EmployeeProfile.objects.get(user=user)
    return employee, user
