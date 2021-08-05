from django.shortcuts import redirect, render, HttpResponse
import random
from time import gmtime, strftime, localtime



def index(request):
    return redirect('/home')

def home(request):
    data = {
    }
    return render(request, 'home.html', data)

def loginPage(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        print('nickname: ', request.POST['nickname'])
        print('goldForm: ', request.POST['goldForm'])
        request.session['nickname'] = request.POST['nickname']
        request.session['goldForm'] = request.POST['goldForm']
        print(request.session['nickname'])
        data = {
            'nickname' : request.session['nickname'],
            'goldForm' : request.session['goldForm']
        }
        return redirect("/process_money")

def logout(request): 
    del request.session['nickname']
    del request.session['goldForm']
    del request.session['gold']
    return redirect('/home')

messages = []
location = ''
timeNow = ''
def processMoney(request):
    if request.method == 'POST':
        print('esto es POST')
        if request.session: #COMO CHUCHA ERA ACA?
            request.session['gold'] = 1
        else:
            if 'gold1020' in request.POST:
                print('Apretaste el gold 10-20')
                number = random.randint(10,20)
                request.session['gold'] += number
                messages.append(number)
                location = 'Farm'
                timeNow = strftime("%b %d, %Y - %H:%M %p", localtime())
                print(messages)
            elif 'gold0510' in request.POST:
                print('Apretaste el gold 05-10')
                number = random.randint(5,10)
                request.session['gold'] += number
                messages.append(number)
                timeNow = strftime("%b %d, %Y - %H:%M %p", localtime())
                location = 'Cave'            
            elif 'gold0205' in request.POST:
                print('Apretaste el gold 02-05')
                number = random.randint(2,5)
                request.session['gold'] += number
                messages.append(number)
                location = 'House'
                timeNow = strftime("%b %d, %Y - %H:%M %p", localtime())
            elif 'goldcasino' in request.POST:
                print('Apretaste el gold CASINO')
                number = random.randint(-50,50)
                request.session['gold'] += number
                messages.append(number)
                location = 'Casino'
                timeNow = strftime("%b %d, %Y - %H:%M %p", localtime())
            data={
                'gold' : request.session['gold'],
                'messages' : messages,
                'location' : location,
                'timenow' : timeNow,
                'nickname' : request.session['nickname'],
                'goldForm' : request.session['goldForm'],
                'goldToWin' : ( int(request.session['goldForm']) - int(request.session['gold']) )
            }
            return render(request, 'index.html', data)
    else:
        print('esto es GET')
        context = {
        'nickname' : request.session['nickname'],
        'goldForm' : request.session['goldForm']
        }
        return render(request, 'index.html', context)
    