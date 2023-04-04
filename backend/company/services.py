from rest_framework.authtoken.models import Token
from .models import CompanyProfile
from users.models import User


def get_company_profile(token):
    user_email = Token.objects.get(key=token).user
    user = User.objects.get(email=user_email)
    company = CompanyProfile.objects.get(user=user)
    return company
