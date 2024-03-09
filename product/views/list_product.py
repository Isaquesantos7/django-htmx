from django.shortcuts import render

def list_product(request):

    return render(request ,'list_product.html', context={})
