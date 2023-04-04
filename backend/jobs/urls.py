from django.urls import path

from .views.list_views import (
    JobListView,
    CompanyJobListView,
    ApplicantsListView
)
from .views.create_views import (
    JobCreateView,
    SavedJobCreateView,
    AppliedJobCreateView
)
from .views.delete_views import JobDeleteView, SavedJobDeleteView
from .views.update_and_details_views import (
    JobUpdateView,
    JobDetailView,
    ApplicantsUpdateView
)
from .views.other_views import (
    JobChoicesView,
    get_total_jobs_and_framework_choices,
    change_job_status,
    get_job_title
)


app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='job_list'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('job_details/<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('update_job/<int:pk>/', JobUpdateView.as_view(), name='job_update'),
    path('delete_job/<int:pk>/', JobDeleteView.as_view(), name='job_delete'),
    path('job_choices/', JobChoicesView.as_view(), name='job_choices'),
    path('get_total_jobs/', get_total_jobs_and_framework_choices, name='get_total_jobs'),
    path('change_job_status/<int:pk>/', change_job_status, name='update_job_status'),
    path('company_job_list/', CompanyJobListView.as_view(), name='company_job_list_create'),
    path('save_job/', SavedJobCreateView.as_view(), name='save_job'),
    path('delete_saved_job/', SavedJobDeleteView.as_view(), name='delete_saved_job'),
    path('apply_job/', AppliedJobCreateView.as_view(), name='apply_job'),
    path('applicants_list/', ApplicantsListView.as_view(), name='applicants_list'),
    path('update_application_status/<int:pk>/', ApplicantsUpdateView.as_view(), name='update_application_status'),
    path('get_job_title/', get_job_title, name='get_job_title')
]