from django.shortcuts import render, HttpResponse
from .models import *


def index(request):
    data = {
        'dojos' : Dojo.objects.all(),
        'ninjas' : Ninja.objects.all()
    }
    return render(request, 'index.html', data)