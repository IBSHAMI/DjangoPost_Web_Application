from django.urls import path, include

from .views import check_if_profile_complete, get_webapp_status_data


app_name = 'users'

urlpatterns = [
    path('check_if_profile_complete/', check_if_profile_complete, name='check_if_profile_complete'),
    path('get_webapp_status_data/', get_webapp_status_data, name='get_webapp_status_data'),
    path('employee/', include('employee.urls')),
    path('company/', include('company.urls')),
]