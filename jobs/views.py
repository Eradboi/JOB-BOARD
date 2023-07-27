from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import *
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from accounts.views import get_user
from django.urls import reverse_lazy, reverse
import logging
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

logger = logging.getLogger(__name__)

class UploadJobView(CreateView, LoginRequiredMixin):
        model = Jobpost
        form_class = JobUploadForm
        template_name = 'jobs/upload.html'
        success_url = reverse_lazy('jobs:jobs_list')



class AllJobsView(ListView):
        model = Jobpost
        template_name = 'jobs/list.html'
        context_object_name = "jobs"
        paginate_by = 10

        def get(self, request, *args, **kwargs):
                # do some logging
                logger.info(f"{request.user} viewed all jobs")
                # return super which will run the default get() method for this class
                return super().get(request, *args, **kwargs)

        def get_queryset(self):
                return Jobpost.objects.order_by('-created_at')

class JobDetailView(DetailView, LoginRequiredMixin):
        model = Jobpost
        template_name = 'jobs/detail.html'

def add_bookmark(request, slug):
        job = get_object_or_404(Jobpost, slug=slug)
        try:
                if Bookmark.objects.get(job=job, user=request.user):
                        messages.info(request, f"This job is in your bookmark")
                        logger.info(f"user {request.user} tried to add {job.title} (which already exist)to their bookmark")
                        return redirect("jobs:jobs_list")
        except ObjectDoesNotExist:
                Bookmark.objects.create(job=job, user=request.user)
                messages.info(request, f"{job.title} has been added to your bookmarks")
                logger.info(f"user {request.user} added {job.title} to their bookmark")
                return redirect("/")
















