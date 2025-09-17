from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# from tenant.models import Store

# Create your models here.

def secondary_email_json():
    return {"secondary_email":[]}

class CustomUser(AbstractUser):
    
    uuid  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    date_of_birth = models.DateField(null=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100, null=True)
    secondary_email = models.JSONField(default=secondary_email_json,null=True)
    
    def __str__(self):
        return self.first_name + ' ' + self.username 
    
    
class EmailTokens(models.Model):
    email = models.EmailField(unique=True)
    token = models.CharField(max_length=9)
    generated_time = models.DateTimeField(auto_now_add=True)
    used_time = models.DateField(null=True)
    isExpired = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    def __str__(self):
        return str(self.email)
    
    
class PhoneTokens(models.Model):
    phone = models.OneToOneField(CustomUser, related_name="phone_token_user", on_delete=models.CASCADE)
    token = models.CharField(max_length=9)
    generated_time = models.DateTimeField(auto_now_add=True)
    used_time = models.DateField(null=True)
    isExpired = models.BooleanField(default=False)
    isVerified = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.phone)
    
    
class Customer(models.Model):
    customer_uuid  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.user) 
    
class Staff(models.Model):
    staff_uuid  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) 
