from django.urls import path, include

from .views import check_if_profile_complete


app_name = 'users'

urlpatterns = [
    path('check_if_profile_complete/', check_if_profile_complete, name='check_if_profile_complete'),
    path('employee/', include('employee.urls')),
    path('company/', include('company.urls')),
]