from django.db import models

from ingredient.models import Ingredient
from sauce.models import Sauce


class Pizza(models.Model):
    name = models.CharField(max_length=50, null=False)
    price = models.DecimalField(decimal_places=0, max_digits=5, null=False)
    ingredients = models.ManyToManyField(Ingredient) # null has no effect on ManyToManyField
    sauce = models.ForeignKey(Sauce, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

