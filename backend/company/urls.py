from django.urls import path, include

from .views import (
    CompanyDetailsAPIView,
)

app_name = 'company'

urlpatterns = [
    path('data/', CompanyDetailsAPIView.as_view(), name='company-data'),
    # path('contact-support/', EmployeeContactSupportAPIView.as_view(), name='employee-contact-support')
]