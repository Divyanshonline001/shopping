from rest_framework import serializers
from . models import Shops

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shops
        fields='__all__'