from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name="index"),
    path('profile/',views.profile,name="profile"),
    path('search/',views.search,name="search"),

    
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin,name="signin"),
    path('signout/',views.signout,name="signout"),
]