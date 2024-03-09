from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

from product.models import Product

@csrf_exempt
@require_http_methods(['DELETE'])
def delete_product(request, index):

    Product.objects.filter(index=index).delete()

    product = Product.objects.all()

    return render(request, 'partials/products.html', context={'product': product})