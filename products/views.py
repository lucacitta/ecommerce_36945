from django.shortcuts import render
from products.models import Products


# Create your views here.
def products(request):
    producto_nuevo = Products.objects.create(
            name = 'Paty',
            price = 550,
            description = 'Que rica y cara esta paty',
            SKU = 'JTGC2454234'
            )
    context = {'producto_nuevo':producto_nuevo}
    return render(request, 'products.html', context=context)