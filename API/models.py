from django.db import models
#unique and randon sku generator
from .utils import unique_sku_generator 
from django.db.models.signals import pre_save,post_save,pre_delete
from django.contrib.auth.models import User
from django.db.models import Q

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



#send post signal to edit remaining item quantity after stock is added
def post_save_item_stock(sender,instance,created,*args, **kwargs):
    item_name = instance.item
    item_id = instance.item.id
    recieved_quantity = instance.recieved_quantity
    items = Item.objects.filter(Q(id = item_id) & Q(item_name = item_name))
    for item in items:
        item.remaining_quantity = item.remaining_quantity + recieved_quantity
        item.is_stock = True
        item.save()



#send post signal to edit remaining item quantity after sale is added or item is sold
def post_save_item_sale(sender,instance,created,*args, **kwargs):
    item_name = instance.item
    item_id = instance.item.id
    sold_quantity = instance.sold_quantity
    items = Item.objects.filter(Q(id = item_id) & Q(item_name = item_name))
    for item in items:
        if item.remaining_quantity >= sold_quantity:
            item.remaining_quantity = item.remaining_quantity - sold_quantity
            if item.remaining_quantity == 0:
                item.is_stock = False
            else:
                item.is_stock = True
            item.save()
        else:#delete that instance
            print("error remaining_quantity is less than sold quantity")
            instance.delete()



pre_save.connect(pre_save_create_new_sku, sender=Item)
post_save.connect(post_save_item_stock,sender=Stock)
post_save.connect(post_save_item_sale,sender=Sale)



#when stock is deleted, reduce it in items
def pre_delete_item_stock(sender,instance,*args, **kwargs):
    item_name = instance.item
    item_id = instance.item.id
    deleted_quantity = instance.recieved_quantity
    items = Item.objects.filter(Q(id = item_id) & Q(item_name = item_name))
    for item in items:
        item.remaining_quantity = item.remaining_quantity - deleted_quantity
        if item.remaining_quantity == 0:
            item.is_stock = False
        else:
            item.is_stock = True
        item.save()



#when sale is deleted, reduce it in items
def pre_delete_item_sale(sender,instance,*args, **kwargs):
    item_name = instance.item
    item_id = instance.item.id
    deleted_quantity = instance.sold_quantity
    items = Item.objects.filter(Q(id = item_id) & Q(item_name = item_name))
    for item in items:
        item.remaining_quantity = item.remaining_quantity + deleted_quantity
        item.save()


pre_delete.connect(pre_delete_item_stock,sender = Stock)
pre_delete.connect(pre_delete_item_sale,sender = Sale)