from django.shortcuts import render

from product.models import Product

def save_product(request):
    name = request.POST.get('name')
    price = request.POST.get('price')

    Product.objects.create(name=name, price=price)
    
    product = Product.objects.all()

    return render(request, 'partials/products.html', context={'product': product})