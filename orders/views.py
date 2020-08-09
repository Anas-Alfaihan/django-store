from django.shortcuts import render, redirect
from carts.models import Cart
from django.contrib.auth.decorators import login_required
from .forms import OrderForm
# Create your views here.


@login_required
def chekout_order(request):
    if request.method == 'POST':
        user = request.user
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save_order(user)
            return render(request, 'orders/check-out-success.html')
    else:
        form = OrderForm()
    return render(request, 'orders/check-out.html', {'form': form})