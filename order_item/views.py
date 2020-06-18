from rest_framework import viewsets, permissions

from order_item.models import OrderItem
from order_item.serializers import OrderItemSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]
