from django.urls import path

from products.views import List_products, Create_product, search_products, Detail_product, Delete_product, Update_product

urlpatterns =[
    path('', List_products.as_view(), name = 'list_products'),

    path('create-products/', Create_product.as_view(), name = 'create_products'),
    path('search-product/', search_products, name = 'search_products'),
    path('detail-product/<int:pk>/', Detail_product.as_view(), name = 'detail_product'),
    path('delete-product/<int:pk>/', Delete_product.as_view(), name = 'delete_product'),
    path('update-product/<int:pk>/', Update_product.as_view(), name = 'update_product'),
]