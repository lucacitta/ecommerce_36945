from django.urls import path

from products.views import list_products, create_products, search_products

urlpatterns =[
    path('', list_products, name = 'products'),

    path('create-products/', create_products, name = 'create_products'),
    path('search-product/', search_products, name = 'search_products'),
]