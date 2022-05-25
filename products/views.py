from django.shortcuts import render
from products.models import Products


# Create your views here.
def products(request):
        products = Products.objects.all()
        context = {'products':products}
        return render(request, 'products.html', context=context)