from django.shortcuts import redirect, render, HttpResponse


def index(request):
    return redirect ('/login')

def loginPage(request): 
    data = {
    }
    if request.method == 'GET':
        return render(request, 'index.html', data)
    else:
        print('Username: ', request.POST['username'])
        print('Password: ', request.POST['password'])
        username_form = request.POST['username']
        password_form = request.POST['password']
        request.session['username'] = username_form
        request.session['password'] = password_form
        return redirect('/success', data)

def success(request):
    data = {
        'username' : request.session['username'],
        'password' : request.session['password']
    }
    return render(request, 'success.html', data)

def logout(request): 
    del request.session['username']
    del request.session['password']
    return redirect('/login')