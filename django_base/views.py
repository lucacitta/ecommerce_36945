from django.http import HttpResponse

from datetime import datetime

from django.template import Template, Context

#from django.shortcuts import render

def saludo(request, nombre):
    return HttpResponse(f'Buenas tardes {nombre} :D')

def despedida(request):
    return HttpResponse('<h1> Nos vemos, fue un gusto :) </h1>')

def fecha_actual(request):
    fecha = datetime.now().date()
    mensaje = f'Hoy es {fecha} !!'
    return HttpResponse(mensaje)

def probandoTemplate(self):

    miHtml = open("C:/Users/Luca/Desktop/Programacion/CodeHouse/Django/ecommerce/templates/template_1.html")

    plantilla = Template(miHtml.read()) #Se carga en memoria nuestro documento, template1   
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close() #Cerramos el archivo

    miContexto = Context() #EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto) #Aca renderizamos la plantilla en documento

    return HttpResponse(documento)

from django.shortcuts import render

def probando_template(request):
    return render(request, 'template_1.html', context = {})