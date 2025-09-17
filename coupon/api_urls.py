from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .api_views import *

from ecommerce.urls import router

# router = DefaultRouter()
router.register(r'coupon/coupons', CouponViewSet, basename='coupons')


urlpatterns = [
    #-----------------customUrl---------------
    path('api/', include(router.urls)),
    
]
