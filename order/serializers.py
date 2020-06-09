from rest_framework import serializers

from order.models import Order
from order_item.models import OrderItem
from order_item.serializers import OrderItemSerializer
from pizza.models import Pizza


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=False)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        print(self.initial_data)
        items = []
        for item in self.initial_data['order_items']:
            # If such an OrderItem is already in the database, do not duplicate it, use the existing one
            db_pizza = db_item = None
            try:
                db_pizza = Pizza.objects.get(name=item['pizza']['name'])
            except Pizza.DoesNotExist:
                raise serializers.ValidationError({'detail': 'that pizza does not exist'})

            try:
                db_item = OrderItem.objects.get(pizza=db_pizza, quantity=item['quantity'])
            except OrderItem.DoesNotExist:
                db_item = OrderItem.objects.create(pizza=db_pizza, quantity=item['quantity'])

            item_to_use = db_item or OrderItem.objects.create(pizza=item['pizza']['name'],
                                                              quantity=item['quantity'])
            items.append(item_to_use)

        new_order = Order.objects.create(address=validated_data['address'],
                                         name=validated_data['name'],
                                         phone=validated_data['phone'],
                                         email=validated_data['email'],
                                         date=validated_data['date'],
                                         due=validated_data['due'])
        new_order.order_items.set(items)
        return new_order
