from django.db import models

# Create your models here.
from customer.models import Customer
from product.models import Product


class Order(models.Model):
    order_number = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"

    def __str__(self):
        return f'[주문번호] {self.order_number} \n ' \
               f'[주문자]{self.customer} \n' \
               f'[주문상품] {self.product}'