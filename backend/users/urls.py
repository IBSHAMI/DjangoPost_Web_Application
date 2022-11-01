from django.urls import path

from .views import (
    EmployeeDetailsAPIView,
)


app_name = 'users'

urlpatterns = [
    # get by pk field to filter
    path('employee/data/', EmployeeDetailsAPIView.as_view(), name='employee-details'),

]