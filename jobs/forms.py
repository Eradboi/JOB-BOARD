from django import forms
from .models import *

class JobUploadForm(forms.ModelForm):
    class Meta:
        model = Jobpost
        fields = ('Title', 'Description', 'Category','Type')

