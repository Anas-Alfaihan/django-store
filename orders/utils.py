from django.template.loader import render_to_string
from .models import Order


def send_order_email(order, total_price):

    subject = 'Your Order Details'
    message = render_to_string('orders/order-email.html',
                               {
                                   'user': order.user,
                                   'order': order,
                                   'total_price': total_price
                               })

    order.user.email_user(subject, message)
