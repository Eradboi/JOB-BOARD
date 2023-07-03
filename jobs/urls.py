from django.urls import path

# importing views from views..py
from .views import UploadJobs, AllJobs

urlpatterns = [
    path('jobs/', UploadJobs.as_view(), name='post-jobs'),
    path('job-list/', AllJobs.as_view(), name='list-jobs'),
]