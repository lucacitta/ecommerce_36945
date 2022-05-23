from django.contrib import admin
from django.urls import path

from django_base.views import saludo, despedida, fecha_actual, probandoTemplate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),
    path('despedida/', despedida, name = 'despedida'),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('probando-template/',probandoTemplate, name = 'probando_template'),   
]