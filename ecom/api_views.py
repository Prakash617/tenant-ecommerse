from django.shortcuts import HttpResponse, render, HttpResponse
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from ecom.models import Product, ProductCategories, Tag
from ecom.serializers import ProductCatagoriesSerializer, ProductSerializer, TagsSerializer
from inventory.models import SupplierData


from .serializers import *



from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import permission_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate





class TagViewSet(viewsets.ModelViewSet):
    queryset= Tag.objects.all()
    serializer_class = TagsSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes =[IsAuthenticated]
    
    def update(self, request, *args, **kwargs):
        data= request.data
        product_category_data = data.pop("product_category")
        try:        
            product_category = ProductCategories.objects.get(category_name = product_category_data["category_name"] )
        except:
            product_category = ProductCategories.objects.create(**product_category_data)
        product = Product.objects.update(**data,product_category = product_category)
        return Response({"updated_data": product})
        

class ProductCatagoriesViewSet(viewsets.ModelViewSet):
    queryset = ProductCategories.objects.all()
    serializer_class = ProductCatagoriesSerializer
    
