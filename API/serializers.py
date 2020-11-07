from rest_framework import serializers
from .models import Vendor,Item,Stock,Sale



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
    
    #in order to show the vendor detail
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['vendor_detail'] = VendorSerializer(instance.vendor).data
        return response

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

    #in order to show the item detail
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['item_detail'] = ItemSerializer(instance.item).data
        return response


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

    #in order to show the item detail
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['item_detail'] = ItemSerializer(instance.item).data
        return response