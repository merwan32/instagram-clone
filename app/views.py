from django.shortcuts import render,redirect
from .models import Profile,Post,Reel,Story
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
# Create your views here.

def index(request):
    profile = Profile.objects.get(user=request.user)
    story = Story.objects.filter(profile__followers=request.user)
    posts = Post.objects.filter(Q(profile__followers=request.user) & ~Q(likes=request.user) | Q(user=request.user) & ~Q(likes=request.user))
    return render(request,'index.html',{'profile':profile,'posts':posts,'stories':story})

def reels(request):
    profile = Profile.objects.get(user=request.user)
    reels = Reel.objects.all()
    return render(request,'reel.html',{'profile':profile,'reels':reels})


def profile(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(user=request.user)
    return render(request,'profile.html',{'profile':profile,'posts':posts})


def edit(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(user=request.user)
    if request.method == 'POST':
        profile.user.username = request.POST['username']
        profile.user.first_name = request.POST['firstname']
        profile.user.last_name = request.POST['lastname']
        profile.bio = request.POST['bio']
        profile.user.save()
        profile.save()
        return render(request,'profile.html',{'profile':profile,'posts':posts})
    else:
        return render(request,'edit.html',{'profile':profile})


def search(request):
    profile = Profile.objects.get(user=request.user)
    search = request.GET['username'] 
    profiles = Profile.objects.filter(user__username__icontains=search)
    
    return render(request,'search.html',{'profile':profile,'profiles':profiles,"username":search})

def change_picture(request):
    profile = Profile.objects.get(user=request.user)
    posts = Post.objects.filter(user=request.user)
    if request.method == "POST":
        pic = request.FILES['img']
        profile.profile_picture  = pic
        profile.save()
        return render(request,'profile.html',{'profile':profile,'posts':posts})
    return render(request,'add/changepicture.html',{'profile':profile})


def follow(request,id,username):
    profile = Profile.objects.get(id=id)
    login_profile = Profile.objects.get(user=request.user)
    if request.user in profile.followers.all():
        profile.followers.remove(request.user)  
        login_profile.followings.remove(profile.user)
    else:
        profile.followers.add(request.user)  
        login_profile.followings.add(profile.user)
    return redirect(f'/search?username={username}')

def upload_post(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        post = request.FILES['img']
        posts = Post.objects.create(user=request.user,profile=profile,image=post)
        return render(request,'profile.html',{'profile':profile})
    return render(request,'add/post.html',{'profile':profile})


def upload_reel(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        reel = request.FILES['reel']
        reels = Reel.objects.create(profile=profile,reel=reel)
        return render(request,'profile.html',{'profile':profile})
    return render(request,'add/reel.html',{'profile':profile})

def upload_story(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        story = request.FILES['story']
        storys = Story.objects.create(profile=profile,story=story)
        return render(request,'profile.html',{'profile':profile})
    return render(request,'add/story.html',{'profile':profile})

    
def like(request,id):
    post = Post.objects.filter(id=id)
    if request.user in post[0].likes.all():
        post[0].likes.remove(request.user)
    else:
        post[0].likes.add(request.user)
    return redirect('index')



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
                user = authenticate(username=username,password=password)
                login(request,user)
                return redirect("index")
    return render(request,'auth/signup.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect("index")
    return render(request,'auth/signin.html')
    
def signout(request):
    logout(request)
    return redirect('signin')