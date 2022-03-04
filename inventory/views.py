from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def inventory(request):
    products = Product.objects.all()
    context = {'products':products}
    if request.method == 'POST':
        try:
            quantity = int(request.POST['quantity'])
        except ValueError:
            context['error_message'] = 'Please enter a valid quantity!'
            return render(request, 'inventory/inventory.html', context)
        for i in range(0, quantity):
            new_product = Product(brand=request.POST['brand'], catagory=request.POST['catagory'], name=request.POST['name'], manufactured=request.POST['manufactured'])
            new_product.save()
    return render(request, 'inventory/inventory.html', context)

def item(request, serial):
    item = get_object_or_404(Product, serial=serial)
    context = {'item':item}
    return render(request, 'inventory/item.html', context)