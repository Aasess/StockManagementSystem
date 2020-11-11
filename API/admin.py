from django.contrib import admin
from .models import Vendor, Category, Item, Stock, Sale
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Category)


class item_admin(ImportExportModelAdmin):
    search_fields = ['sku', 'item_name', 'category__category_name', 'price', 'vendor__name', 'is_stock', 'created_at', 'created_by']
    fields = ['item_name', 'category', 'price', 'vendor']
    list_display = ['sku', 'item_name', 'category', 'price', 'vendor', 'remaining_quantity', 'is_stock', 'created_at', 'updated_at', 'created_by']

    # ADDING CURRENT USER TO created_by column when adding item
    def save_model(self, request, obj, form, change):
        # if(getattr(obj, 'created_by') is None):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
admin.site.register(Item, item_admin)


class vendor_admin(admin.ModelAdmin):
    fields = ['name', 'address', 'phone']
    list_display =  ('name', 'address', 'phone', 'created_at', 'updated_at', 'created_by')

    # ADDING CURRENT USER TO created_by column when adding item
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
admin.site.register(Vendor, vendor_admin)


class stock_admin(ImportExportModelAdmin):
    fields = ['item', 'recieved_quantity']
    list_display = ['item', 'recieved_quantity', 'created_at', 'updated_at', 'created_by']
    # auto_complete = ['item']

    # ADDING CURRENT USER TO created_by column when adding item
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
admin.site.register(Stock, stock_admin)


class sale_admin(ImportExportModelAdmin):
    fields = ['item', 'sold_quantity']
    list_display = ['item', 'sold_quantity', 'created_at', 'updated_at', 'created_by']

    # ADDING CURRENT USER TO created_by column when adding item
    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        obj.save()
admin.site.register(Sale, sale_admin)
# admin.site.register(Sale)
