"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework.routers import DefaultRouter
from user_accounts.api_views import *



# router = DefaultRouter()
from ecommerce.urls import router
router.register(r'user_accounts/staff/register', StaffCreatViewSet, basename='register_staff')
router.register(r'user_accounts/login', LoginViewSet, basename='login')
router.register(r'user_accounts/user', UserList, basename='User')
router.register(r'changepassword', UserChangePasswordView, basename='changepassword')
router.register(r'send-reset-password-email', SendPasswordResetEmailView, basename='send-reset-password-email')
router.register(r'reset-password', UserPasswordResetView, basename='reset-password'),



urlpatterns = [
    # ------------------jwt------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #-----------------customUrl---------------
    path('api/', include(router.urls)),
    
]
