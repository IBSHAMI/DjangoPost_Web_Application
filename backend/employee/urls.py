from django.urls import path, include

from .views import (
    EmployeeDetailsAPIView,
    EmployeeContactSupportAPIView,
    EmployeeChoicesView,
    EmployeeProfilePictureAPIView,
    EmployeeProfileResumeAPIView,
)

app_name = 'employee'

urlpatterns = [
    path('data/', EmployeeDetailsAPIView.as_view(), name='employee-data'),
    path('contact-support/', EmployeeContactSupportAPIView.as_view(), name='employee-contact-support'),
    path('employee_choices/', EmployeeChoicesView.as_view(), name='employee_choices'),
    path('employee_profile_picture/', EmployeeProfilePictureAPIView.as_view(), name='employee_profile_picture'),
    path('employee_profile_resume/', EmployeeProfileResumeAPIView.as_view(), name='employee_profile_resume'),
]
