from django.urls import path

from .views import *

urlpatterns = [
    path('list/product/', list_product, name='list_products'),

    # endpoints
    path('check/product/', check_product, name='check_product'),
    path('save/product/', save_product, name='save_product'),
    path('delete/product/<int:index>/', delete_product, name='delete_product'),
]