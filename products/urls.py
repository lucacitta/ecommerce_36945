from django.urls import path

from products.views import products

urlpatterns =[
    path('', products, name = 'products'),
]