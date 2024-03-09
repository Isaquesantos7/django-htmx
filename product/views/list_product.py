from django.shortcuts import render

from product.models import Product

def list_product(request):
    product = Product.objects.all()

    return render(request ,'list_product.html', context={'product': product})
