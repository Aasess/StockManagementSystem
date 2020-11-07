from django.db import models
#unique and randon sku generator
from .utils import unique_sku_generator 
from django.db.models.signals import pre_save

# Create your models here.

class Vendor(models.Model):
    name = models.CharField(max_length = 200,blank=True,null=True) 
    address = models.CharField(max_length = 200,blank=True,null=True)
    phone = models.CharField(max_length = 15,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.name



class Category(models.Model):
    category_name =  models.CharField(max_length=200)
    def __str__(self):
        return self.category_name


class Item(models.Model):
    stock_choices = (
        (0,'Out of Stock'),
        (1,'In Stock')
    )

    sku = models.CharField(max_length=15, blank= True)
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, #one category has many items
        on_delete = models.SET_NULL, #if category is deleted, set the category_id to null
        null = True,
        related_name = "items_cat"
    )
    price = models.FloatField(default=0)
    vendor = models.ForeignKey(
        Vendor, #one vendor has many items
        on_delete = models.SET_NULL,
        null = True,
        related_name = "items_vendor"
    )
    remaining_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)
    is_stock = models.IntegerField(choices = stock_choices)

    def __str__(self):
        return self.item_name

    def check_instock(self):
        if(self.remaining_quantity > 0 ):
            return True

class Stock(models.Model):
    item = models.ForeignKey(
        Item, #one item has many stocks left
        on_delete = models.SET_NULL,
        null = True,
        related_name = "stocks"
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)
    recieved_quantity = models.IntegerField(default=0)

   

class Sale(models.Model):
    item = models.ForeignKey(
        Item, #one item is sold to many
        on_delete = models.SET_NULL,
        null = True,
        related_name = "sales"
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)
    sold_quantity = models.IntegerField(default=0)




def pre_save_create_new_sku(sender, instance, *args, **kwargs):
    if not instance.sku:
        instance.sku= unique_sku_generator(instance)

pre_save.connect(pre_save_create_new_sku, sender=Item)

