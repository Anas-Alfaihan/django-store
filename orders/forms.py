from django.forms import ModelForm
from .utils import send_order_email
from django.db.models import Sum
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('address',)

    def save_order(self, user):
        self.instance.user = user
        self.instance.save()
        self.instance.items.set(user.cart.items.all())

        total_price = self.instance.items.aggregate(Sum('price'))['price__sum']

        send_order_email(self.instance, total_price)

        user.cart.items.clear()