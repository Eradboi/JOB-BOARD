from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import User
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def get_user(request):
    user = User.objects.get(username=request.user.username)
    return user

def display_user_name(request):
    return render(request, 'user.html')

def signup_view(request):
    if request.method == 'POST':
        form = NewUSerForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('account_login')
    else:
        form = NewUSerForm()

    context = {
        'form': form
    }
    return render(request, 'registrations/signup.html', context)

class CompleteProfileView(View, LoginRequiredMixin):
    def get(self, request, *args, **kwargs):
        try:
            context = {
                'profile': get_user(request),
            }
            return render(self.request, 'registrations/complete_profile.html', context)
        except ObjectDoesNotExist:
            return HttpResponse(request, 'THIS USER HAS NO PROFILE')

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            twitter = request.POST['twitter']
            print(twitter)
            user = get_user(request)
            user.twitter = twitter
            user.save()
            return redirect('account_login')


