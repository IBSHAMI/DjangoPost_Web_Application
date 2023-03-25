from django.urls import path

from .views import (
    JobListView,
    CompanyJobListView,
    JobCreateView,
    JobDetailView,
    JobUpdateView,
    JobDeleteView,
    JobChoicesView,
    change_job_status
)

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('job_details/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('update_job/<int:pk>/', JobUpdateView.as_view(), name='job_update'),
    path('delete_job/<int:pk>/', JobDeleteView.as_view(), name='job_delete'),
    path('job_choices/', JobChoicesView.as_view(), name='job_choices'),
    path('change_job_status/<int:pk>/', change_job_status, name='update_job_status'),
    path('company_job_list/', CompanyJobListView.as_view(), name='company_job_list_create'),
]