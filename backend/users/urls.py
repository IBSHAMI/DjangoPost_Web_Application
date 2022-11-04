from django.urls import path, include


app_name = 'users'

urlpatterns = [
    path('employee/', include('employee.urls')),
]