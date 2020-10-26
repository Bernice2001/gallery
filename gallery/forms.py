from django import forms
from django.forms import ModelForm
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
