from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Profile,Image
from .forms import NewImageForm,NewProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return render(request,'home.html')

def user_profile(request):
  profile = Profile.objects.all()
  post = Image.objects.all()

  return render(request,'insta.html',{"profile":profile,"post":post})

@login_required(login_url='/accounts/login')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewImageForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.profile = current_user
      post.save()
    return redirect('userProfile')

  else:
    form = NewImageForm()
  return render(request,'new_post.html',{"form":form})



