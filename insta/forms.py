from django import forms
from .models import Profile,Image

class NewImageForm(forms.ModelForm):
  class Meta:
    model=Image
    exclude = ['profile','name']

class NewProfileForm(forms.ModelForm):
  class Meta:
    model=Profile
    exclude = ['user']