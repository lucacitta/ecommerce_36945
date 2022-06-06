from django.contrib import admin

from products.models import Products, Categoria

# Register your models here.
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'SKU', 'is_active']



admin.site.register(Categoria)