from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

from products.models import Products
from products.forms import Product_form

def contacto(request):
    return render(request, 'contacto.html')


# Create your views here.
def products(request):
    productos = Products.objects.all()
    context = {'productos':productos}
    return render(request, 'products.html', context=context)


def create_product_view(request):
    if request.method == 'GET':
        form = Product_form()
        context = {'form':form}
        return render(request, 'create_product.html', context=context)
    else:
        form = Product_form(request.POST)
        if form.is_valid():
            new_product = Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context ={'new_product':new_product}
        else:
            context ={'errors':form.errors}
        return render(request, 'create_product.html', context=context)

def search_product_view(request):
    #product = Products.objects.get()
    palabra_busqueda = request.GET['search']
    products = Products.objects.filter(name__icontains = palabra_busqueda)
    if products.exists():
        context = {'products':products}
    else:
        context = {'errors':f'Disculpe, no se encontro ningun producto con la palabra clave: {palabra_busqueda}'}
    return render(request, 'search_product.html', context = context)