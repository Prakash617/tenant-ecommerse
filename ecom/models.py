
from django.db import models
import uuid
from user_accounts.models import Customer
   

# from user_accounts.models import User, CustomUser
# Create your models here.
Stockchoice = (
    ('IS', 'instock'),
    ('OFS', 'outofstock')
)
Product_type = (
    ('sp', 'simpleproduct'), ('vp', 'variableproduct')
)
Price_type = (
    ('rp', 'regularprice'), ('sp', 'saleprice')
)



    
def category_image():
    return {"category_image":[]}

class ProductCategories(models.Model):
    category_name = models.CharField(max_length=100,null=True,unique=True, blank=True)
    category_image = models.URLField( null=True ,blank= True)
    
    def __str__(self):
        return self.category_name

def image_gallery_json():
    return  {"image_gallery":[]}
def product_attribute_data():
    return  {"product_attribute_data":[]}


def codes():
    return  {"codes":{'qr_link':'',
                      'bar_code_link':''
                      }}

class Product(models.Model):
    uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    SKU = models.CharField(max_length=50,unique=True, null=True,blank=True)
    name = models.CharField(max_length=50)
    regular_price = models.FloatField()
    sell_price = models.FloatField()
    # /////////////
    product_category = models.ForeignKey(ProductCategories, on_delete=models.CASCADE, null=True)
    # /////////////////
    main_image  =  models.URLField(max_length = 200,default='main_image')
    image_gallery = models.JSONField(default=image_gallery_json)
    stock_status = models.CharField(choices=Stockchoice, max_length=50)
    description = models.TextField()
    purchase_note = models.CharField(max_length=100)
    minimum_order_limit = models.IntegerField()
    stock_quentity = models.IntegerField()
    
    isVisible = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    product_type = models.CharField(choices=Product_type, max_length=50)
    
    product_attribute_data = models.JSONField(default=product_attribute_data)
    
    isAffiliate = models.BooleanField(default=False)
    product_discounted_price = models.FloatField()
    codes = models.JSONField(default=codes)
    product_link = models.URLField()
    data_published = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    
def product_attribute_values():
    return {"values":[]}
class ProductAttributes(models.Model):
    product = models.ForeignKey(Product, related_name="product_attributes", on_delete=models.CASCADE ,null=True)
    attribute_name = models.CharField(max_length=100)
    attribute_type = models.CharField(max_length= 100)
    values = models.JSONField(default=product_attribute_values)
    default_value = models.CharField(max_length=100)
    
class Tag(models.Model):
    product = models.ManyToManyField(Product)
    tag = models.CharField(max_length=75 ,unique=True)
    
    def __str__(self):
        return self.tag
    
class Review(models.Model):
    product = models.ForeignKey(Product,related_name='review_product',null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(Customer, related_name='reviewing_customer', on_delete=models.CASCADE)
    star_count = models.IntegerField()
    review_text = models.CharField(max_length=100)
    review_media = models.URLField()
    
    def __str__(self):
        return self.name
    
class ProductQueries(models.Model):
    product = models.ForeignKey(Product,related_name='query_product',null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(Customer, related_name='query_customer', on_delete=models.CASCADE)
    question = models.CharField(max_length=999)
    answer = models.CharField(max_length=999)
   
    
    def __str__(self):
        return self.name
    
    