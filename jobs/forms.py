from django import forms
from .models import Upload

class JobUploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('Title', 'Description','Duration','Onsite')

