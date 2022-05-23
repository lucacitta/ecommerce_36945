from django.contrib import admin
from django.urls import path

from django_base.views import saludo, despedida, fecha_actual, probando_template
from products.views import products


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),
    path('despedida/', despedida, name = 'despedida'),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
    path('probando-template/', probando_template, name = 'probando_template'),
    path('products/', products, name = 'products'),
]