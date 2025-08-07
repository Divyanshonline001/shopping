from django.shortcuts import render

# Create your views here.

from . serializers import ShopSerializer
from . models import Shops
from rest_framework import viewsets

class ShopViewSet(viewsets.ModelViewSet):
    queryset=Shops.objects.all()
    serializer_class=ShopSerializer

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')