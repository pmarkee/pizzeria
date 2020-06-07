from django.shortcuts import render

from rest_framework import viewsets

from sauce.serializers import SauceSerializer
from sauce.models import Sauce


class SauceViewSet(viewsets.ModelViewSet):
    queryset = Sauce.objects.all()
    serializer_class = SauceSerializer

