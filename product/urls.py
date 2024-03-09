from django.urls import path

from .views import *

urlpatterns = [
    path('list/product/', list_product, name='list_products')
]