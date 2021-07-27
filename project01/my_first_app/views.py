from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def indexPrueba(request):
    return HttpResponse("I'm your first Django Project! 🐍")

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse('placeholder para luego mostrar una lista de todos los blogs')

def new(request):
    return HttpResponse('placeholder para mostrar un nuevo formulario para crear un nuevo blog')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f'placeholder para mostrar el blog numero: {number}')

def edit(request, number):
    return HttpResponse(f'placeholder para editar el blog {number}')

def destroy(request, number):
    return redirect('/blogs')

def jsonf(request):
    data = {
        'name': 'John Doe',
        'age': 69420,
        'job': 'Software Engineer'
    }
    return JsonResponse(data)



