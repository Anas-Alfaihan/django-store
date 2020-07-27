from django.urls import path
from .views import add_to_cart, cart, remove_from_cart, remove_all


urlpatterns = [
    path('', cart, name='cart'),
    path('remove_all', remove_all, name='remove_all'),
    path('add/<product_id>', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<product_id>', remove_from_cart, name='remove_from_cart')
]
