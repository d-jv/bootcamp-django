from django import shortcuts
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit', views.edit),
    path('shows/<int:show_id>/update', views.update),
    path('shows/new', views.newShow),
    path('add_show', views.addShow),
    # path('remove/<int:network_id>/<int:show_id>', views.remove),
    path('remove/<int:show_id>', views.remove),
]