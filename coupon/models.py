from django.db import models

# Create your models here.
coupon_types = (
    ('percentage_discount', 'Percentage_Discount'),
    ('flat_discount', 'Flat_Discount'),
    ('buy_one_get_one', 'Buy_One_Get_One'),
    ('free_shipping', 'Free_Shipping'),
   
)
class Coupon(models.Model):
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=100,choices=coupon_types)
    coupon_details=models.JSONField()