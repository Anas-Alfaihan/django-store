from django.db import models
from django.urls import reverse


# Create your models here.


class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('product_details', args=(self.id, ))

    def __str__(self):
        return self.title
