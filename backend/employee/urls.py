from django.urls import path, include

from .views import (
    EmployeeDetailsAPIView,
    EmployeeContactSupportAPIView,
)

app_name = 'employee'

urlpatterns = [
    path('data/', EmployeeDetailsAPIView.as_view(), name='employee-data'),
    path('contact-support/', EmployeeContactSupportAPIView.as_view(), name='employee-contact-support')
]
