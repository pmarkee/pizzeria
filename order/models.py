from django.db import models
from django.db.models import OneToOneField, ManyToManyField, ForeignKey

from order_item.models import OrderItem
from pizza.models import Pizza


class Order(models.Model):
    address = models.CharField(max_length=300, null=False)
    name = models.CharField(max_length=300, null=False)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(null=True)
    date = models.DateTimeField(null=False)
    due = models.DateTimeField(null=False)
    order_items = ManyToManyField(OrderItem)

    def __str__(self):
        return self.name
