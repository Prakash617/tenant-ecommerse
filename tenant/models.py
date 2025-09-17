from django.db import models

# Create your models here.
from django_tenants.models import TenantMixin, DomainMixin

# from user_accounts.models import CustomUser

# Create your models here.

class StoreCategory(models.Model):
    store_catagory_name = models.CharField(max_length=99)
    
    def __str__(self):
        return self.store_catagory_name
    
class StoreUnit(models.Model):
    unit = models.CharField(max_length=10)
    store_catogory = models.ForeignKey(StoreCategory,related_name="store_category", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.unit +' ' + str(self.store_catogory)
    
class Store(TenantMixin):
    store_name = models.CharField(max_length=99)
    store_category = models.OneToOneField(StoreCategory,on_delete=models.CASCADE,null=True)
    store_logo = models.URLField(blank=True ,null=True)

    store_email = models.EmailField(blank=True)
    store_url = models.URLField(blank=True,null=True)
    store_visit_count = models.IntegerField(blank=True)
    active_theme = models.CharField(max_length=99,blank=True)
    store_owner = models.OneToOneField('user_accounts.CustomUser', related_name="store_admin", null=True, on_delete=models.CASCADE,blank=True)
    
    def __str__(self):
        return self.store_name
    
    
class Domain(DomainMixin):
    pass

