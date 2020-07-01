from django.shortcuts import render, get_object_or_404
from .models import Product
from django.utils import timezone


# Create your views here.

def products_list(request):
    products = Product.objects.all()
    if len(products):
        return render(request, 'products/products-list.html', {'products': products})
    else:
        return render(request, 'products/products-emlist.html')


def show_time(request):
    time_now = timezone.now()
    return render(request, 'show-time.html', {'time': time_now})


def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product-details.html', {'product': product})
