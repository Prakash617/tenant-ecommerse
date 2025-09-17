from django.shortcuts import HttpResponse, render, HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from ecom.models import Product, ProductCategories, Tag
from ecom.serializers import ProductCatagoriesSerializer, ProductSerializer, TagsSerializer
from inventory.models import SupplierData
from user_accounts.models import CustomUser, Staff

from .serializers import *

from inventory.serializers import (
    SupplySerializer,
    SupplierSerializer
)


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = SupplierData.objects.all()
    serializer_class = SupplierSerializer


        
        
class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer