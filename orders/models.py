from django.db import models
from django.contrib.auth import get_user_model
from products.models import Product
# Create your models here.
User = get_user_model()
class Order(models.Model):
    address = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='order', on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)