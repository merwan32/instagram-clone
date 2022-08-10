from django.shortcuts import render,redirect
from .models import Profile
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'index.html',{'profile':profile})

def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile.html',{'profile':profile})

def search(request):
    profile = Profile.objects.get(user=request.user)
    search = request.GET['username']
    profiles = Profile.objects.filter(user__username__icontains=search)
    return render(request,'search.html',{'profile':profile,'profiles':profiles})
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password != cpassword :
            messages.success(request,"password doesn't match")
            return render(request,'auth/signup.html')
        else:
            user = User.objects.create_user(username=username,email=email,password=password)
            profil = Profile.objects.create(user=user)
            if profil :
                messages.success(request,'profile created please login')
                return redirect("signin")
    return render(request,'auth/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("profile")
    return render(request,'auth/signin.html')
    
def signout(request):
    logout(request)
    return redirect('signin')