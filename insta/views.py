from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Profile,Image
from .forms import NewImageForm,NewProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return render(request,'home.html')

def user_profile(request):
  profiles = Profile.objects.all()
  posts = Image.objects.all()
  profile_pic = profiles.reverse()[0:1]

  return render(request,'insta.html',{"profile_pic":profile_pic,"posts":posts})

@login_required(login_url='/accounts/login')
def new_post(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewImageForm(request.POST,request.FILES)
    if form.is_valid():
      post = form.save(commit=False)
      post.user = current_user
      post.save()
    return redirect('userProfile')

  else:
    form = NewImageForm()
  return render(request,'new_post.html',{"form":form})

@login_required(login_url='/accounts/login')
def profile(request):
  current_user = request.user
  if request.method == 'POST':
    form = NewProfileForm(request.POST,request.FILES)
    if form.is_valid():
      profile = form.save(commit=False)
      profile.user = current_user
      profile_pic = form.cleaned_data['profile_pic']
      bio = form.cleaned_data['bio']
      update = Profile.objects.filter(user=current_user).update(bio=bio,profile_pic=profile_pic)
      profile.save(update)
    return redirect('userProfile')

  else:
    form = NewProfileForm()
  return render(request,'profile.html',{"form":form})



