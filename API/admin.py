from django.contrib import admin
from .models import Vendor, Item, Stock, Sale
# Register your models here.
admin.site.register(Vendor)
# admin.site.register(Item)
admin.site.register(Stock)
admin.site.register(Sale)

class item_search(admin.ModelAdmin):
    search_fields = ['item_name','price']

admin.site.register(Item, item_search)



