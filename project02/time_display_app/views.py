from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime, localtime


def index(request):
    return redirect('/time_display')

def displayTimeDate(request):
    data = {
        "day": strftime("%b %d, %Y", localtime()),
        "time": strftime("%H:%M %p", localtime()),
        "AMorPM": strftime('%p', localtime()),
    }
    return render(request, 'index.html', data)
