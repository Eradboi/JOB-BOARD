from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import *
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from accounts.views import get_user
from django.urls import reverse_lazy, reverse
import logging

# Create your views here.

logger = logging.getLogger(__name__)

class UploadJobsView(CreateView, LoginRequiredMixin):
        model = Upload
        form_class = JobUploadForm
        template_name = 'jobs/upload.html'
        success_url = reverse_lazy('jobs:jobs_list')



class AllJobsView(ListView, LoginRequiredMixin):
        model = Upload
        template_name = 'jobs/list.html'
        paginate_by = 10

        def get(self, request, *args, **kwargs):
                # do some logging
                logger.info(f"{request.user} view all jobs")
                # return super which will run the default get() method for this class
                return super().get(request, *args, **kwargs)










