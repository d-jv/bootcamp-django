from django import shortcuts
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.newShow),
]