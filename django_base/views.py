from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def saludo(request, nombre):
    return HttpResponse(f'Buenas tardes {nombre} :D')

def despedida(request):
    return HttpResponse('<h1> Nos vemos, fue un gusto :) </h1>')

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'Hoy es {fecha} !!'
    return HttpResponse(mensaje)

def probando_template(request):
    return render(request, 'template_1.html', context = {})
