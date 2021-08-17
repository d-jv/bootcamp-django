from django.urls import path     
from . import views
from .models import Wizard



urlpatterns = [
    path('', views.index),	   
]

