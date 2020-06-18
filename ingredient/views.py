from django.shortcuts import render

from rest_framework import viewsets, permissions

from ingredient.serializers import IngredientSerializer
from ingredient.models import Ingredient


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]