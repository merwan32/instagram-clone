from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name="index"),
    path('profile/',views.profile,name="profile"),
    path('search/',views.search,name="search"),
    path('reels/',views.reels,name="reels"),
    path('follow/<int:id>/<str:username>/',views.follow,name="follow"),
    path('uploadpost/',views.upload_post,name="upload_post"),
    path('like/<int:id>/',views.like,name="like"),
    path('uploadreel/',views.upload_reel,name="upload_reel"),
    path('uploadstory/',views.upload_story,name="upload_story"),
    path('edit/',views.edit,name="edit"),
    
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
]