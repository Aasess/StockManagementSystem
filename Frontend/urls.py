from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "home"),

    path('item',views.item, name = "item"),
    path('item_add',views.item_add, name = "item_add"),

    path('vendor',views.vendor, name = "vendor"),
    path('sale',views.sale, name = "sale"),
    path('stock',views.stock, name = "stock"),
]
