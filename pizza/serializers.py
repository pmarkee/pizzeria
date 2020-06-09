from rest_framework import serializers

from ingredient.models import Ingredient
from ingredient.serializers import IngredientSerializer
from pizza.models import Pizza
from sauce.models import Sauce
from sauce.serializers import SauceSerializer


class PizzaSerializer(serializers.ModelSerializer):
    sauce = SauceSerializer(read_only=False)
    ingredients = IngredientSerializer(read_only=False, many=True)

    class Meta:
        model = Pizza
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        print(validated_data)
        pizza_name = validated_data.get('name')
        pizza_price = validated_data.get('price')
        pizza_sauce = Sauce.objects.get(name=validated_data.get('sauce').get('name'))
        pizza_ingredients = []
        for item in validated_data.get('ingredients'):
            pizza_ingredients.append(Ingredient.objects.get(name=item.get('name')))
        new_pizza = Pizza.objects.create(name=pizza_name, price=pizza_price, sauce=pizza_sauce)
        new_pizza.ingredients.set(pizza_ingredients)
        return new_pizza
