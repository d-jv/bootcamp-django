from django.shortcuts import redirect, render, HttpResponse



def index(request):
    return redirect('/shows')

def shows(request):
    data = {

    }
    return render(request, 'shows.html', data)

def newShow(request):
    data = {

    }
    return render(request, 'newShow.html', data)
