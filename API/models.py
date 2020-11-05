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
    updated_by = models.CharField(max_length = 200,blank=True)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    category_choice = [
        ['Medicine','Medicine'],
        ['Paste','Paste'],
        ['Brush','Brush']
    ]

    stock_choices = (
        (0,'Out of Stock'),
        (1,'In Stock')
    )

    sku = models.CharField(max_length=15, blank= True)
    item_name = models.CharField(max_length=200)
    category = models.CharField(choices = category_choice,max_length = 200,blank=True,null=True)
    price = models.FloatField(default=0)
    vendor = models.ForeignKey(
        Vendor, #one vendor has many items
        on_delete = models.CASCADE,
        related_name = "items"
    )
    remaining_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length = 200,blank=True)
    is_stock = models.IntegerField(choices = stock_choices)

    def __str__(self):
        return self.item_name

    def check_instock(self):
        if(self.remaining_quantity > 0 ):
            return True

class Stock(models.Model):
    item = models.ForeignKey(
        Item, #one item has many stocks left
        on_delete = models.CASCADE,related_name="stocks"
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)
    updated_by = models.CharField(max_length = 200,blank=True)
    recieved_quantity = models.IntegerField(default=0)

   

class Sale(models.Model):
    item = models.ForeignKey(
        Item, #one item is sold to many
        on_delete = models.CASCADE,related_name="sales"
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)
    updated_by = models.CharField(max_length = 200,blank=True)
    sold_quantity = models.IntegerField(default=0)



# class Employee(models.Model):
#     name = models.CharField(max_length = 200)
#     phone = models.CharField(max_length = 15)
#     address = models.CharField(max_length = 200)
#     password = models.CharField(max_length = 200,default='')

def pre_save_create_new_sku(sender, instance, *args, **kwargs):
    if not instance.sku:
        instance.sku= unique_sku_generator(instance)

pre_save.connect(pre_save_create_new_sku, sender=Item)

