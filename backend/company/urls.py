from django.urls import path, include

from .views import (
    CompanyDetailsAPIView,
    CompanyProfileLogoAPIView
)

app_name = 'company'

urlpatterns = [
    path('data/', CompanyDetailsAPIView.as_view(), name='company-data'),
    path('company_profile_logo/', CompanyProfileLogoAPIView.as_view(), name='company_profile_logo'),
]