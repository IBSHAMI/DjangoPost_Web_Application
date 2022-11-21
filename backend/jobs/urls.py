from django.urls import path

from .views import (
    JobListView,
    JobCreateView,
    JobDetailView,
    JobUpdateView,
    JobDeleteView,
    JobChoicesView,
)

app_name = 'jobs'

urlpatterns = [
    path('', JobListView.as_view(), name='job_list_create'),
    path('create/', JobCreateView.as_view(), name='job_create'),
    path('<int:pk>/', JobDetailView.as_view(), name='job_detail'),
    path('<int:pk>/update/', JobUpdateView.as_view(), name='job_update'),
    path('<int:pk>/delete/', JobDeleteView.as_view(), name='job_delete'),
    path('job_choices/', JobChoicesView.as_view(), name='job_choices'),

]