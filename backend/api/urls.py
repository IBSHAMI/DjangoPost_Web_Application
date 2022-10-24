from django.urls import path, include

app_name = 'api'

urlpatterns = [
    path('jobs/', include('jobs.urls')),
    path('users/', include('users.urls')),
]