from django.urls import path
from .views import *


urlpatterns = [
    path('', display_user_name, name="user_name"),
    path('signup/', signup_view, name="sign_up"),
    path('complete-profile/', CompleteProfileView.as_view(), name="complete_profile"),
]