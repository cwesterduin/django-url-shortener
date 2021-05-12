from django import forms
from .models import Url

class NewUrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = ['url']