from django.contrib import admin
from .models import Vendor, Item, Stock, Sale
# Register your models here.
admin.site.register(Vendor)
# admin.site.register(Item)
admin.site.register(Stock)
admin.site.register(Sale)

class item_search(admin.ModelAdmin):
    search_fields = ['sku', 'item_name', 'category', 'price', 'vendor', 'remaining_quantity', 'is_stock', 'created_user']
    # fields = ('sku', 'item_name', 'price')
    list_display = ('sku', 'item_name', 'price')

admin.site.register(Item, item_search)



