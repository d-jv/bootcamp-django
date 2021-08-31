from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.login),
    path('create_account', views.create_account),
    path('logout', views.logout),
    path('post', views.postMsg),
]