from django.shortcuts import render
from .models import Product
from django.utils import timezone


# Create your views here.

def  products_list(request):
    products = Product.objects.all()
    return render(request, 'products-list.html', {'products': products})

def show_time(request):
    time_now = timezone.now()
    return render(request, 'show-time.html', {'time': time_now})