from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products
from products.forms import Product_form


# Create your views here.       
def list_products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'products.html', context=context)

def detail_product(request, pk):
    try:
        product = Products.objects.get(id=pk)
        context = {'product':product}
        return render(request, 'product_detail.html', context=context)
    except:
        context = {'error':'El Producto no exixste'}
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
                is_active = form.cleaned_data['is_active'],
            )
            context = {'new_product':new_product}
        else:
            context = {'errors':form.errors}
        return render(request, 'create_products.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')

def search_products(request):
    products = Products.objects.filter(name__icontains=request.GET['search'])
    if products.exists():
        context = {'products':products}
    else:
        context = {'errors':'No se encontro el producto'}
    return render(request, 'search_products.html', context = context)