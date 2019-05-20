from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Profile,Image
from .forms import NewImageForm,NewProfileForm

# Create your views here.
def home(request):
  return render(request,'home.html')

def user_profile(request):
  profile = Profile.objects.all()
  post = Image.objects.all()

  return render(request,'insta.html',{"profile":profile,"post":post})


