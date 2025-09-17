from .serializers import OrderSerializer
from .models import *
from rest_framework import viewsets
from django.contrib.auth import authenticate


class OrderViewSet(viewsets.ModelViewSet):
    queryset=Orders.objects.all()
    serializer_class=OrderSerializer
