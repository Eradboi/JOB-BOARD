from django import forms
from .models import *

class JobUploadForm(forms.ModelForm):
    class Meta:
        model = Jobpost
        fields = ('title', 'description', 'category','type')

