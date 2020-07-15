from django.shortcuts import render, get_object_or_404
from .models import Product
from django.utils import timezone
from .forms import AddProductForm
from django.shortcuts import redirect

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


def product_add(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'products/product-add-successful.html')
    else:
        form = AddProductForm()
    return render(request, 'products/product-add.html', {'form': form})


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = AddProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return render(request, 'products/product-add-successful.html')
    else:
        form = AddProductForm(instance=product)
    return render(request, 'products/product-add.html', {'form': form})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('products_list')
