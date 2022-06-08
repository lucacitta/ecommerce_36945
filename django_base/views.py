from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}!! :D'}
                return render(request, 'index.html', context = context)
            else:
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context)

def logout_view(request):
    logout(request)
    return redirect('index')

def index(request):
    print(request.user)
    print(request.user.is_authenticated)
    return render(request, 'index.html')








def saludo(request, nombre):
    return HttpResponse(f'Buenas tardes {nombre} :D')



def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'Hoy es {fecha} !!'
    return HttpResponse(mensaje)

def probando_template(request):
    context = {
        'nombre':'Luca',
        'apellido':'Citta Giordano',
        'fecha':datetime.now(),
        'edades':[18,20,5,10,12,17,22,40]
    }
    return render(request, 'template_1.html', context = context)

def contact(request):
    return render(request, 'contact.html')
