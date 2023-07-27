from django.urls import path

# importing views from views.py
from .views import *

app_name = "jobs"

urlpatterns = [
    path('jobs/', UploadJobView.as_view(), name='jobs_post'),
    path('job-list/', AllJobsView.as_view(), name='jobs_list'),
    path('job-detail/<str:title>/<str:slug>/', JobDetailView.as_view(), name="job_detail"),
    path('bookmark/add/<str:slug>/', add_bookmark, name="add_bookmark"),
]