from django.shortcuts import render

# Create your views here.

from . serializers import ShopSerializer
from . models import Shops
from rest_framework import viewsets

class ShopViewSet(viewsets.ModelViewSet):
    queryset=Shops.objects.all()
    serializer_class=ShopSerializer