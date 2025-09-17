
from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter

router = DefaultRouter()



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecom/',include('ecom.api_urls')),
    path('inventory/',include('inventory.api_urls')),
    path('users/',include('user_accounts.api_urls')),
    path('orders/',include('orders.api_urls')),
    path('coupons/',include('coupon.api_urls')),
    path('tenant/',include('tenant.api_urls')),
    path('api/', include(router.urls)),
]
