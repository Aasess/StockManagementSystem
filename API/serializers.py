from rest_framework import serializers
from .models import Vendor,Item,Stock,Sale



class VendorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name','address','phone','updated_by']
