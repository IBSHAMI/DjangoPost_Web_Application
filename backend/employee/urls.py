from django.urls import path, include

from .views import EmployeeDetailsAPIView

app_name = 'employee'

urlpatterns = [
    path('data/', EmployeeDetailsAPIView.as_view(), name='employee-data')
]
