from django.db import models

from pizza.models import Pizza


class Order(models.Model):
    address = models.CharField(max_length=300, null=False)
    name = models.CharField(max_length=300, null=False)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(null=True)
    date = models.DateTimeField(null=False)
    due = models.DateTimeField(null=False)
    pizzas = models.ManyToManyField(Pizza) # null has no effect on ManyToManyField

    def __str__(self):
        return self.name