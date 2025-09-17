from django.db import models
from ecom.models import Product
from user_accounts.models import Customer
from coupon.models import Coupon

# Create your models here.

order_status = (
    ('pending_payment', 'Pending Payment'),
    ('processing', 'Processing'),
    ('on_hold', 'On_hold'),
    ('completed', 'Completed'),
    ('cancelled', 'Cancelled'),
    ('refunded', 'Refunded'),
    ('failed', 'Failed'),
    ('draft', 'Draft'),
)
class Payment_Gateway(models.Model):
    name=models.CharField(max_length=100,null=True)
    key=models.JSONField(null=True)


class Orders(models.Model):
    order_product = models.ForeignKey(Product, related_name="order_product", on_delete=models.CASCADE)
    order_quantity = models.IntegerField()
    order_contact = models.CharField(max_length=20)
    shipping_address = models.CharField(max_length=50)
    coupon=models.ForeignKey(Coupon,on_delete=models.CASCADE,related_name="coupons",null=True)
    order_status = models.CharField(choices=order_status,max_length=45)
    order_datetime = models.DateField(auto_now_add=True)
    applied_cupons = models.CharField(max_length=100)
    delivery_amount= models.FloatField(null=True)
    totol_amount = models.FloatField()
    grand_total= models.FloatField(null=True)
    payment_info=models.ForeignKey(Payment_Gateway,on_delete=models.CASCADE,related_name="payments",null=True)
    customer = models.ForeignKey(Customer, related_name="order_customer", on_delete=models.CASCADE)
    

