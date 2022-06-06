from django.urls import path

from products import views

urlpatterns =[
    path('', views.list_products, name = 'products'),
    path('list-products-api-view/', views.list_products_api_view.as_view(), name = 'list_products_api_view'),

    path('create-product/', views.create_products, name = 'create_products'),
    path('create-product-api-view/', views.create_product_api_view.as_view(), name = 'create_product_api_view'),

    path('detail-product/<int:pk>/', views.detail_product, name = 'detail_product'),
    path('detail-product-api-view/<int:pk>/', views.detail_product_api_view.as_view(), name = 'detail_products_api_view'),


    path('update-product-api-view/<int:pk>/', views.update_product_api_view.as_view(), name = 'update_products_api_view'),


    path('delete-product-api-view/<int:pk>/', views.delete_product_api_view.as_view(), name = 'delete_products_api_view'),    

    path('search-product/', views.search_products, name = 'search_products'),
]