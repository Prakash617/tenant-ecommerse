from rest_framework import serializers
from .models import (
    Supply,
    SupplierData
)

class SupplierSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SupplierData
        fields = ["name","contact","email","address"]


class SupplySerializer(serializers.ModelSerializer):

    supplier = SupplierSerializer(many=False)

    def create(self, validated_data):
        supplier_data = validated_data.pop("supplier")
        # print(supplier_data["name"])
        try:
            supplier = SupplierData.objects.get(name=supplier_data["name"])
        except:
            supplier = SupplierData.objects.create(**supplier_data)
        
        new_data = Supply.objects.create(**validated_data, supplier = supplier)
        
        return new_data
    
    class Meta:
        model = Supply
        fields = ['product_name','price','unit','unit_value','supplier']






















