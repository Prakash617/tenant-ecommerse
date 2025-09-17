from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model= Orders
        fields= '__all__'