from django.core.exceptions import ValidationError
from django.shortcuts import redirect, render, HttpResponse
from .models import *
from django.db.utils import IntegrityError
from django.contrib import messages
import bcrypt


def index(request):
    return redirect('/home')

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
        'username': user.username,
        'email': user.email,
        'avatar': user.avatar
    }
    messages.success(request, f'Hello there! {user.username}')
    return redirect('/shows')

def logout(request):
    del request.session['user']
    return redirect('/home')

def create_account(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        # si llega por un POST, tomar valores del formulario
        # y crear un nuevo usuario
        username = request.POST['username']
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
        user = User.objects.create(
            username=username,
            email=email,
            password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        )
        request.session['user'] = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'avatar': user.avatar
        }
        messages.success(request, 'User successfully created')
        return redirect('/shows')


def show(request, id):
    show = Show.objects.get(id=id)
    data = {
        'show' : show
    }
    return render(request, 'show.html', data)

def edit(request, id):
    show = Show.objects.get(id=id)
    time_str = show.release_date.strftime('%Y-%m-%d')
    data = {
        'show' : show,
        'time_str' : time_str
    }
    return render(request, 'edit.html', data)

def shows(request):
    data = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', data)

def newShow(request):
    data = {
        'networks' : Network.objects.all()
    }
    return render(request, 'newShow.html', data)

def addShow(request):
    if request.POST['network_id'] == 'other':
        # en este caso hay que crearla
        new_network_name = request.POST['newNetwork']
        network = Network.objects.create(name = new_network_name)
    else:
        #pescar lo que venga del network id y traer el network
        # en este caso hay que rescatarla de la DB
        network_id = request.POST['network_id']
        network = Network.objects.get(id=network_id)
    # -------

    showTitle = request.POST['title']
    showDate = request.POST['date']
    showDesc = request.POST['desc']
    show = Show.objects.create(title = showTitle, release_date = showDate, desc = showDesc)
    show.networks.add(network)
    return redirect(request.META.get('HTTP_REFERER'))

# def remove(request, show_id, network_id):
def remove(request, show_id):
    show = Show.objects.get(id=int(show_id))
    # network = Network.objects.get(id=int(network_id))
    # show_id = int(request.POST['show-id'])
    # show = Show.objects.get(id=show_id)
    # print(show)
    #Network.shows.remove(show)
    show.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def removeNetwork(request, network_id):
    network = Network.objects.get(id=int(network_id))
    # network = Network.objects.get(id=int(network_id))
    # show_id = int(request.POST['show-id'])
    # show = Show.objects.get(id=show_id)
    # print(show)
    #Network.shows.remove(show)
    network.delete()
    return redirect(request.META.get('HTTP_REFERER'))

def update(request, show_id):
    # if request.POST['network_id'] == 'other':
    #     # en este caso hay que crearla
    #     new_network_name = request.POST['newNetwork']
    #     network = Network.objects.create(name = new_network_name)
    # else:
    #     # en este caso hay que rescatarla de la DB
    #     network_id = request.POST['network_id']
    #     network = Network.objects.get(id=network_id)
    # # -------
    # show = Show.objects.get(id=int(show_id))
    # showTitle = request.POST['title']
    # showDate = request.POST['date']
    # showDesc = request.POST['desc']
    # show.title = showTitle
    # show.release_date = showDate
    # show.desc = showDesc
    # show.networks.add(network)  ###????? mejorar esta wea
    # show.save()
    ##### ---------------- Metodo 2 acá abajo --------------
    show = Show.objects.get(id=int(show_id))
    showTitle = request.POST['title']
    showDate = request.POST['date']
    showDesc = request.POST['desc']
    show.title = showTitle
    show.release_date = showDate
    show.desc = showDesc
    new_network_name = request.POST['newNetwork']
    if new_network_name == "":
        pass
    else:
        # network = Network.objects.create(name = new_network_name)
        # show.networks.add(network)
        try:
            if Network.objects.filter(name=new_network_name).exists():
                print('YA EXISTE')
                alreadyExist = Network.objects.filter(name=new_network_name)
                print(alreadyExist)
            else:
                network = Network.objects.create(name = new_network_name)
                show.networks.add(network)
                messages.success(request, f'Show {show.title} has been updated')
        except IntegrityError:
            messages.error(request, 'This Network already exist')
            return redirect(request.META.get('HTTP_REFERER'))
    show.save()
    return redirect(request.META.get('HTTP_REFERER'))