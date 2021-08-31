from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.db.utils import IntegrityError
from django.contrib import messages
import bcrypt
from .decorators import *
from time import gmtime, strftime, localtime




def home(request):
    data = {}
    return render(request, 'home.html', data)

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        messages.error(request, 'Wrong user/password')
        return redirect('/home')

        # si llegamos acá, estamos seguros que al  menos el usuario SI existe
    if  not bcrypt.checkpw(password.encode(), user.password.encode()): 
        messages.error(request, "Wrong user/password")
        return redirect('/home')
    
        # si llegamos hasta acá, estamos seguros que es el usuario y la contraseña está correcta
    request.session['user'] = {
        'id': user.id,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'avatar': user.avatar
    }
    messages.success(request, f'Hello there, {user.first_name} {user.last_name}!')
    return redirect('/')

def logout(request):
    del request.session['user']
    return redirect('/home')

def create_account(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        # si llega por un POST, tomar valores del formulario
        # y crear un nuevo usuario
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_check = request.POST['password_check']

        # validar que el formulario esté correcto
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            # en este caso, hay al menos 1 error en el formulario
            # voy a mostrarle los errores al usuario
            for llave, mensaje_de_error in errors.items():
                messages.error(request, mensaje_de_error)
        
            return redirect('/home')
        
        # si llegamos hasta acá, estamos seguros que ambas coinciden
        try:
            user = User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            )
            request.session['user'] = {
                'id': user.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'avatar': user.avatar
            }
            messages.success(request, 'User successfully created')
            messages.success(request, f'Welcome to CodingDojo Wall, {user.first_name} {user.last_name}.')
            return redirect('/')
        except IntegrityError:
            messages.error(request, 'This email is already in use')
            return redirect(request.META.get('HTTP_REFERER'))

@login_required
def index(request):
    data = {
        'posts': posts
    }
    return render(request, 'index.html', data)

posts = []
@login_required
def postMsg(request):
    post_msg = request.POST['post_msg']
    user_session = request.session['user']
    # print(user_session['email'])
    user = User.objects.get(email=user_session['email'])
    timeNow = strftime("%b %d, %Y - %H:%M %p", localtime())
    new_post = Message.objects.create(
        message = post_msg,
        user = user
    )
    full_msg = {
        'author': f'{user.first_name} {user.last_name} - {timeNow}',
        'message': new_post.message
    }
    posts.insert(0, full_msg)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def postComment(request):
    pass