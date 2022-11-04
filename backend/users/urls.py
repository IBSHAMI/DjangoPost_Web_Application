from django.urls import path

from .views import (
    EmployeeDetailsAPIView,
    # EmployeeResumeAPIView,
)


app_name = 'users'

urlpatterns = [
    # get by pk field to filter
    path('employee/data/', EmployeeDetailsAPIView.as_view(), name='employee-data'),
    # path('employee/resume/', EmployeeResumeAPIView.as_view(), name='employee-resume'),
]