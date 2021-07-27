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

def home(request):
    context = {
        'name' : 'Diego',
        'images': [
            'https://i.redd.it/ln618pt684b71.jpg',
            'https://preview.redd.it/x79lx9zfq7971.jpg?width=640&crop=smart&auto=webp&s=3773a95e6d398571fbe27cd1a4e6c4fb6db2a591',
            'https://preview.redd.it/oorz4pzakpb71.jpg?width=640&crop=smart&auto=webp&s=0c2c9295055c943e4eecc028afc3b1f22ed977c0',
            'https://preview.redd.it/hqz0luk4wjc71.jpg?width=640&crop=smart&auto=webp&s=5c9cc33e697bf5960a7d93d463a2e7c97220520d',

        ]
    }
    return render(request, 'home.html', context)




