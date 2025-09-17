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

from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import permission_required
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate


import json




def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

# # Create your views here.
class UserList(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [AllowAny]
    
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
    
class LoginViewSet(viewsets.ModelViewSet):
    
    queryset = CustomUser.objects.all()
    serializer_class = UserLoginSerializer

    
    # def list(self, request, *args, **kwargs):
    #     try:
    #         user = request.user
    #     except: 
    #         user = {"error":"login_required"}
    #     return Response({"user":user})
    def list(self, request, *args, **kwargs):
        # print(dir(request.user))
        if request.user.is_authenticated:
            print(request.user)
            return Response({"data":request.user})
        return Response({"error":"login_required"})
    

    def create(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        # username = serializer.data.get('username')
        # password = serializer.data.get('password')
        # user = authenticate(username=username, password=password)
        # if user is not None:
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':f'Login Success', 'uuid': user.uuid}, status=status.HTTP_200_OK)
        # else:
            # return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
    
    

class UserChangePasswordView(viewsets.ModelViewSet):

    permission_classes = [IsAuthenticated]
    authentication_classes=[JWTAuthentication]
    
    def create(self, request, *args, **kwargs):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Changed Successfully'}, status=status.HTTP_200_OK)
    
    
class SendPasswordResetEmailView(viewsets.ModelViewSet):
#   renderer_classes = [UserRenderer]
    def create(self, request, *args, **kwargs):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
    
class UserPasswordResetView(viewsets.ModelViewSet):
#   renderer_classes = [UserRenderer]


  def create(self, request, uid=None,*args, **kwargs):
    # print("uid",uid)
    # print('User password reset',request.query_params.get('id'))
    uid = request.query_params.get('uid')
    token = request.query_params.get('token')
    print('User password reset',uid,'token',token)
    # uid = kwargs['uid']
    # token = kwargs['token']
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    serializer.is_valid(raise_exception=True)
    return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)

class StaffCreatViewSet(viewsets.ModelViewSet):
    # queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    
    def get_queryset(self):
        staff = Staff.objects.all()
        return staff
        # return super().get_queryset(staff,user)


    def list(self, request , *args, **kwargs):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many = True)
    
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            
        user_detail = request.data
        
        new_user = CustomUser.objects.create(
            password=password,username=user_detail['username'],first_name=user_detail['first_name'],last_name=user_detail['last_name'],email=user_detail['email'],is_staff=user_detail['is_staff'],is_active=user_detail['is_active'],date_of_birth=user_detail['date_of_birth'],phone=user_detail['phone'],address=user_detail['address'],secondary_email=user_detail['secondary_email']
                )
        Staff.objects.create(user=new_user)
    
        return Response({'message':'success'})