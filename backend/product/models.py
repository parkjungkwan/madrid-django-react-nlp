from django.db import models
import json
# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'vendors'

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    currencies = [
        ('W', "Korean Won (W)"),
    ]
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    currency = models.CharField(max_length=5, choices=currencies, default="$")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(default="not_found.jpg")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('name',)
        db_table = 'products'

