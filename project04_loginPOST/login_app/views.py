from django.shortcuts import redirect, render, HttpResponse


def index(request):
    return redirect ('/login')

data = []
def loginPage(request): 
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        #user = next((u for u in USERS if u['nombre'] == name_from_form), None)
        print('Username: ', request.POST['username'])
        print('Password: ', request.POST['password'])
        # username_form = request.POST['username']
        # password_form = request.POST['password']
        # request.session['username'] = username_form
        # request.session['password'] = password_form
        data.append(dict({request.POST['username']:request.POST['password']}))
        request.session['username'] = request.POST['username']
        request.session['password'] = request.POST['password']
        print('---------------Antes de mostrar el Data------------')
        print(data)
        print('---------------Despues de mostrar el Data------------')
        return redirect('/success')

def success(request):
    context = {
        'username' : request.session['username'],
        'password' : request.session['password']
    }
    return render(request, 'success.html', context)

def logout(request): 
    del request.session['username']
    del request.session['password']
    return redirect('/login')