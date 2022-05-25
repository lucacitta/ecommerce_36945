from django.contrib import admin
from django.urls import path

from django_base.views import saludo, despedida, fecha_actual, probando_template
<<<<<<< HEAD
=======
from products.views import products
>>>>>>> main


urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/<nombre>/', saludo, name = 'saludo'),
    path('despedida/', despedida, name = 'despedida'),
    path('fecha_actual/', fecha_actual, name = 'fecha_actual'),
<<<<<<< HEAD
    path('probando-template/',probando_template, name = 'probando_template'),   
=======
    path('probando-template/', probando_template, name = 'probando_template'),
    path('products/', products, name = 'products'),
>>>>>>> main
]