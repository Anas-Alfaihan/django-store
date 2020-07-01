from django.urls import path
from .views import products_list, show_time, product_details


urlpatterns = [
    path('products/', products_list, name='products_list'),
    path('time/', show_time),
    path('product/<pk>', product_details, name='product_details')
]
