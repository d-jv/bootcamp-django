from django import shortcuts
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.newShow),
    path('add_show', views.addShow),
    # path('remove/<int:network_id>/<int:show_id>', views.remove),
    path('remove/<int:show_id>', views.remove),
]