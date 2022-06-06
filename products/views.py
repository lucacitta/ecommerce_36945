from django.http import HttpResponse
from django.shortcuts import render

from products.models import Products
from products.forms import Product_form

from django.urls import reverse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def list_products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'products/products.html', context=context)

def create_products(request):
    if request.method == 'GET':

        form = Product_form()
        context = {'form':form}

        return render(request, 'products/create_products.html', context=context)

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
        return render(request, 'products/create_products.html', context = context)

    else:
        return HttpResponse('Only GET and POST methods are allowed')

def search_products(request):
    if not request.GET['search'] == '':
        products = Products.objects.filter(name__icontains=request.GET['search'])
        if products.exists():
            context = {'products':products}
        else:
            context = {'errors':'No se encontro el producto'}
    else:
        context = {'errors':'Debes enviar un texto por el cual filtrar'}
    return render(request, 'products/search_products.html', context = context)


class list_products_api_view(ListView):
    model = Products
    template_name = 'products/products.html'
    queryset = Products.objects.filter(is_active=True)


class detail_product_api_view(DetailView):
    model = Products
    template_name = 'products/product_detail.html'


class update_product_api_view(UpdateView):
    model = Products
    template_name = 'products/update_product.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_products_api_view', kwargs={'pk': self.object.pk} )


class create_product_api_view(CreateView):
    model = Products
    template_name = 'products/create_products.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detail_products_api_view', kwargs={'pk': self.object.pk} )


class delete_product_api_view(DeleteView):
    model = Products
    template_name = 'products/product_delete.html'

    def get_success_url(self):
        return reverse('list_products_api_view')
