from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products
from products.forms import Product_form


# Create your views here.       
def list_products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'products.html', context=context)

def create_products(request):
    if request.method == 'GET':

        form = Product_form()
        context = {'form':form}

        return render(request, 'create_products.html', context=context)

    elif request.method == 'POST':
        
        form = Product_form(request.POST)
        if form.is_valid():
            new_product = Products.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                SKU = form.cleaned_data['SKU'],
                active = form.cleaned_data['active'],
            )
            context = {'new_product':new_product}
        else:
            context = {'errors':form.errors}
        return render(request, 'create_products.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')

def search_products(request):
    print(request.GET)
    try:
        product = Products.objects.get(name__in=request.GET['search'])
        context = {'product':product}
        return render(request, 'search_products.html', context = context)
    except:
        context = {'errors':'No se encontro el producto'}
        return render(request, 'search_products.html', context = context)
