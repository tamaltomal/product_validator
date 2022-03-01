from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def inventory(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'inventory/inventory.html', context)

def item(request, serial):
    item = get_object_or_404(Product, serial=serial)
    context = {'item':item}
    return render(request, 'inventory/item.html', context)