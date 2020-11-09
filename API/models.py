from django.db import models
#unique and randon sku generator
from .utils import unique_sku_generator 
from django.db.models.signals import pre_save,post_save,post_delete
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import DatabaseError

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
    sku = models.CharField(max_length=15, blank= True)
    item_name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, #one category has many items
        on_delete = models.SET_NULL, #if category is deleted, set the category_id to null
        null = True,
        blank = True,
        related_name = "items_cat"
    )
    price = models.PositiveIntegerField(default=0)
    vendor = models.ForeignKey(
        Vendor, #one vendor has many items
        on_delete = models.SET_NULL,
        null = True,
        blank = True,
        related_name = "items_vendor"
    )
    remaining_quantity = models.PositiveIntegerField(default=0)
    is_stock = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)

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
    recieved_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)

   

class Sale(models.Model):
    item = models.ForeignKey(
        Item, #one item is sold to many
        on_delete = models.SET_NULL,
        null = True,
        related_name = "sales"
        )
    sold_quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length = 200)


#send pre signal to generate unique sku value before saving item	
def pre_save_create_new_sku(sender, instance, *args, **kwargs):	
    if not instance.sku:	
        instance.sku= unique_sku_generator(instance)


def stock_calculate_signal(sender,instance,*args, **kwargs):
    item_name = instance.item
    item_id = instance.item.id
    items = Item.objects.filter(Q(id = item_id) & Q(item_name = item_name))
    sold_items_sum =  0
    recieved_items_sum = 0
    for item in items:
        sold_items = item.sales.all()
        recieved_items = item.stocks.all()

    for sold_item in sold_items:
        sold_items_sum = sold_items_sum + sold_item.sold_quantity

    for recieved_item in recieved_items:
        recieved_items_sum = recieved_items_sum + recieved_item.recieved_quantity
    
    item = Item.objects.get(pk = item_id)
    if(recieved_items_sum > sold_items_sum):
        item.remaining_quantity = recieved_items_sum - sold_items_sum
        item.is_stock = True
        item.save()
    
    elif(recieved_items_sum == sold_items_sum):
        item.remaining_quantity = 0
        item.is_stock = False
        item.save()
    else:
        raise DatabaseError("sold quantity cannot be greater than stock")



#signals
post_save.connect(stock_calculate_signal,sender = Stock)
post_save.connect(stock_calculate_signal,sender = Sale)

post_delete.connect(stock_calculate_signal,sender = Stock)
post_delete.connect(stock_calculate_signal,sender = Sale)

pre_save.connect(pre_save_create_new_sku, sender=Item)
