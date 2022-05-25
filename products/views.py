from django.shortcuts import render
from products.models import Products


# Create your views here.
def products(request):
        productos = Products.objects.all()
        context = {'productos':productos}
        return render(request, 'products.html', context=context)