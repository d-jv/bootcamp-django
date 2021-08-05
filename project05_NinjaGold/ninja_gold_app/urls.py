from django.urls import path     
from . import views


urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('login', views.loginPage),	
    path('process_money', views.processMoney),
    path('logout', views.logout),
]