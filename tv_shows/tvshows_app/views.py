from django.shortcuts import redirect, render, HttpResponse
from .models import *


def index(request):
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

def update(request, show_id):
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
    show = Show.objects.get(id=int(show_id))
    showTitle = request.POST['title']
    showDate = request.POST['date']
    showDesc = request.POST['desc']
    show.title = showTitle
    show.release_date = showDate
    show.desc = showDesc
    show.networks.add(network)
    show.save()
    return redirect(request.META.get('HTTP_REFERER'))