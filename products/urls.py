from django.urls import path

from products.views import list_products, create_products, search_products, detail_product

urlpatterns =[
    path('', list_products, name = 'products'),

    path('create-products/', create_products, name = 'create_products'),
    path('search-product/', search_products, name = 'search_products'),
    path('detail-product/<int:pk>/', detail_product, name = 'detail_product'),
]