from .models import *
from rest_framework import serializers



class StoreCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= StoreCategory
        fields= '__all__'


class StoreUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model= StoreUnit
        fields= '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model= Store
        fields= '__all__'
