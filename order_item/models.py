from django.db import models
from django.db.models import ForeignKey

from pizza.models import Pizza


class OrderItem(models.Model):
    pizza = ForeignKey(Pizza, on_delete=models.CASCADE, null=False)
    quantity = models.DecimalField(decimal_places=0, max_digits=2)

    def __str__(self):
        return "%s %s db" % (str(self.pizza), self.quantity)
