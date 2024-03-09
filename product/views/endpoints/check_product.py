from django.shortcuts import render

from product.models import Product

def check_product(request):
    name = request.GET.get('name')

    product = Product.objects.filter(name=name)

    return render(request, 'partials/components/badge.html', context={'product': product})