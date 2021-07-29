from django.shortcuts import redirect, render, HttpResponse
from django.utils.crypto import get_random_string



def index(request):
    return redirect('/random_word')


def wordGenerator(request):
    counter = request.session.get('counter')
    if counter is None:
        request.session['counter'] = 1
        random_message = get_random_string(length=32)

    elif counter >= 10:
        request.session['counter'] = 10
        random_message = '❌No tienes mas intentos...'
    else:
        request.session['counter'] +=1
        random_message = get_random_string(length=32)

    data = {
        'random_word': random_message,
        'counter': counter,
    }
    return render(request, 'index.html', data)

def resetCounter(request):
    request.session['counter'] = 1
    return redirect('/random_word')
