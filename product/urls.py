from django.urls import path

from .views import *

urlpatterns = [
    path('list/product/', list_product, name='list_products'),

    # endpoints
    path('check/product/', check_product, name='check_product'),
]