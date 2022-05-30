from django.urls import path

from products.views import products, contacto

urlpatterns =[
    path('', products, name = 'products'),
    path('contacto/', contacto, name = 'contacto')
]