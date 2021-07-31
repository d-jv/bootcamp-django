from django.urls import path     
from . import views



urlpatterns = [
    path('success', views.success),
    path('', views.index),
    path('login', views.loginPage),
    path('logout', views.logout),
]