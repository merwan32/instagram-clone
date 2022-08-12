from django.db import models
from django.contrib.auth.models import User
# Create your models here...
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    followers = models.ManyToManyField(User,related_name="followers",blank=True)
    followings = models.ManyToManyField(User,related_name="followings",blank=True)
    profile_picture = models.ImageField(upload_to='profilepics',default='profilepics/default-user.png')

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    likes = models.ManyToManyField(User,related_name="likes")


class Reel(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    reel = models.FileField(upload_to='reels')
    likes = models.ManyToManyField(User,blank=True)