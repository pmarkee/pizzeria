from django.shortcuts import render

from rest_framework import viewsets

from order.serializers import OrderSerializer
from order.models import Order


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

