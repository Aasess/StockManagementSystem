from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),
    # path('item',views.item, name = "item"),

    path('item_add',views.item_add, name = "item_add"),
    path('vendor',views.vendor, name = "vendor"),
    path('vendor_add',views.vendor_add,name = "vendor_add"),
    path('sale',views.sale, name = "sale"),
    path('sale_add',views.sale_add,name = "sale_add"),
    path('stock',views.stock, name = "stock"),
    path('stock_add',views.stock_add,name = "stock_add"),
    path('category_add',views.category_add,name="category_add"),
    path('stock_add_modal',views.stock_add_direct,name="stock_add_direct"),
    path('sale_add_modal',views.sale_add_direct,name="sale_add_direct"),
    path('record',views.record,name="record") 
]
