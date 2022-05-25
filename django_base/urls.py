from django.contrib import admin
from django.urls import path

from django_base.views import saludo, index, fecha_actual, probando_template
from products.views import products


urlpatterns = [
    path('', index, name = 'index'),
    
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),

    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('probando-template/', probando_template, name = 'probando_template'),
    path('products/', products, name = 'products'),
]