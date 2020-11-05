from rest_framework import serializers
from .models import Vendor,Item,Stock,Sale



class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name','address','phone','updated_by']


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name','category','price','vendor','remaining_quantity','updated_by','is_stock']
    
    #in order to show the vendor detail
    def to_representation(self,instance):
        response = super().to_representation(instance)
        response['vendor_detail'] = VendorSerializer(instance.vendor).data
        return response