from django.contrib import admin
from .models import Vendor,Item,Stock
# Register your models here.
admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(Stock)