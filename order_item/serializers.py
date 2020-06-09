from rest_framework import serializers

from order_item.models import OrderItem
from pizza.models import Pizza
from pizza.serializers import PizzaSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    pizza = PizzaSerializer(many=False, read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'
        extra_kwargs = {
            'pizza': {'validators': []}
        }

    def create(self, validated_data):
        print(self.initial_data)
        existing_pizza = Pizza.objects.get(name=self.initial_data['pizza']['name'])
        return OrderItem.objects.create(pizza=existing_pizza, quantity=self.initial_data['quantity'])
