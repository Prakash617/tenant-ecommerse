from .models import Coupon
from rest_framework import viewsets
from .serializers import CouponSerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset=Coupon.objects.all()
    serializer_class=CouponSerializer
