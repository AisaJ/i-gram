from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Profile,Image
from .forms import NewImageForm,NewProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
  return render(request,'home.html')

def user_profile(request):
  current_user = request.user
  profiles = Profile.objects.filter(user_id=current_user.id)[0:1]
  posts = Image.objects.filter(user_id=current_user.id)  

  return render(request,'insta.html',{"profile_pic":profiles,"posts":posts})

def feeds(request):  
  profiles = Profile.objects.all()
  posts = Image.objects.all()
  return render(request,'feeds.html',{"posts":posts,"profiles":profiles})

def comments(request):
  return render(request,'feeds.html')


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
      Profile.objects.filter(user=current_user).update(bio=bio,profile_pic=profile_pic)
      profile.save()
    return redirect('userProfile')

  else:
    form = NewProfileForm()
  return render(request,'profile.html',{"form":form})



