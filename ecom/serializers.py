from ecom.models import Product, ProductAttributes, ProductCategories, Tag
from inventory.models import SupplierData, Supply
from user_accounts.models import *
from rest_framework import serializers, viewsets
from django.contrib.auth import authenticate


class ProductCatagoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategories
        fields = "__all__"
        
        
class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributes
        fields = "__all__"
        
        
class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"  
        
        
class ProductSerializer(serializers.ModelSerializer):
    product_category = ProductCatagoriesSerializer(many= False , required = False )
    # read_only =True
    class Meta:
        model = Product
        fields = "__all__"
        
        
    def create(self, validated_data):
        product_category_data = validated_data.pop("product_category")
        # tags_data = validated_data.pop("tags")
        try:
            product_category = ProductCategories.objects.get(category_name = product_category_data["category_name"] )
        except:
            product_category = ProductCategories.objects.create(**product_category_data)
            
        product = Product.objects.create(**validated_data,product_category = product_category)
            
        
        return product
        # supplier_data = validated_data.pop('supplier')
      
        # try:
        #     supplier = SupplierData.objects.get(phone=supplier_data["phone"])
        # except:
        #     supplier = SupplierData.objects.create(**supplier_data)
        
        # new_data = Supply.objects.create(**validated_data, supplier = supplier)
        
        # return new_data
        
        # return super().create(validated_data)
        
        
    def update(self, instance, validated_data):
        product_category_data = validated_data.pop("product_category")
        product_category_obj = ProductCategories.objects.get(category_name = product_category_data["category_name"] )

    #    
        # -------to update nested serializers

        # product_catagory = instance.product_category
        # for k, v in product_catagory_data.items():
        #     setattr(product_catagory, k, v)
        # product_catagory.save()
        
        for k, v in validated_data.items():
            instance.k = v
        #     setattr(Product, k, v)
        # product_catagory.save()
       
        instance.product_category = product_category_obj
        # instance.save()
        instance.save(**validated_data)
        return instance
        
    # def update(self, instance, validated_data):