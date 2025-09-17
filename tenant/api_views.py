from django.shortcuts import HttpResponse, render, HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets

from tenant.models import Store


from .serializers import *

from .models import *
from .serializers import *
from rest_framework import viewsets

class StoreCategoryViewSet(viewsets.ModelViewSet):
    queryset=StoreCategory.objects.all()
    serializer_class=StoreCategorySerializer


class StoreUnitViewSet(viewsets.ModelViewSet):
    queryset=StoreCategory.objects.all()
    serializer_class=StoreCategorySerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset=Store.objects.all()
    serializer_class=StoreSerializer

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer