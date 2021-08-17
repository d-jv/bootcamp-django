from django.shortcuts import render, HttpResponse
from .models import Wizard


def index(request):
    data = {
        'wizards': Wizard.objects.all()
    }
    return render (request, 'index.html', data)