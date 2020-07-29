from django.urls import path
from .views import chekout_order


urlpatterns = [
    path('order/new/', chekout_order, name='checkout_order')
]
