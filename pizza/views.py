from django.shortcuts import render

from rest_framework import viewsets

from pizza.models import Pizza
from pizza.serializers import PizzaSerializer


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all().order_by('id')
    serializer_class = PizzaSerializer
