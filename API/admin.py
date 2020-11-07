from django.contrib import admin
from .models import Vendor, Category, Item, Stock, Sale
# Register your models here.
admin.site.register(Category)
admin.site.register(Stock)
admin.site.register(Sale)

class item_admin(admin.ModelAdmin):
    search_fields = ['sku', 'item_name', 'category__category_name', 'price', 'vendor__name', 'is_stock', 'created_at', 'created_by']
    fields = ['item_name', 'category', 'price', 'vendor']
    list_display = ['sku', 'item_name', 'category', 'price', 'vendor', 'remaining_quantity', 'is_stock', 'created_at', 'updated_at', 'created_by']

    # ADDING CURRENT USER TO created_by column when adding item
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        obj.save()

admin.site.register(Item, item_admin)


class vendor_admin(admin.ModelAdmin):
    list_display =  ('name', 'address', 'phone', 'created_at', 'updated_at', 'created_by')
    
admin.site.register(Vendor, vendor_admin)
