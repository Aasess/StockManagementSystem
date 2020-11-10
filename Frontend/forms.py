from django import forms
from API.models import Category,Vendor,Item
from django.core.exceptions import ValidationError
from django.db.models import Q

class ItemAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ItemAddForm, self).__init__(*args, **kwargs)
        self.fields['vendor'] = forms.ChoiceField(label="Select Vendor",choices=[('','-------------------')]+[(x.id,x.name) for x in Vendor.objects.all()])
        self.fields['category'] = forms.ChoiceField(label="Select Category",choices=[('','-------------------')]+[(x.id,x.category_name) for x in Category.objects.all()])


    item_name  = forms.CharField(label='Item Name', max_length=200)
    try:
        category = forms.ChoiceField(label="Select Category",choices=[('','-------------------')]+[(x.id,x.category_name) for x in Category.objects.all()])
    except:
        category = forms.ChoiceField(choices = [('','---------------------')])
    price = forms.IntegerField(widget=forms.NumberInput)
    try:
        vendor = forms.ChoiceField(label="Select Vendor",choices=[('','-------------------')]+[(x.id,x.name) for x in Vendor.objects.all()])
    except:
        vendor = forms.ChoiceField(choices = [('','---------------------')])
    
    price.widget.attrs.update(
        {
            'min': 0
        }
    )
   
   
    def clean(self):
        cleaned_data = super().clean()
        itemname = cleaned_data['item_name']
        categoryid = cleaned_data['category']
        vendorid = cleaned_data['vendor']
        
        cat = Category.objects.get(pk = categoryid)
        vendor = Vendor.objects.get(pk = vendorid)
        
        try:
            item = Item.objects.get(Q(item_name__iexact = itemname) & Q(category = cat) & Q(vendor = vendor))
            raise ValidationError("Error!! Item already exists with same category name and vendor name.")
        except Item.DoesNotExist:
            pass            
        


class VendorAddForm(forms.Form):
    name = forms.CharField(label='Vendor Name', max_length=200)
    address = forms.CharField(max_length=200,required = False)
    phone = forms.CharField(max_length=14,required = False)


    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Vendor.objects.get(name__iexact = name)
            raise ValidationError("Error!! Vendor already exists.")
        except Vendor.DoesNotExist:
            return name



class StockAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StockAddForm, self).__init__(*args, **kwargs)
        self.fields['itemid'] = forms.ChoiceField(label="Select Item Name",choices=[('','-------------------')]+[(x.id,f"{x.item_name} - {x.vendor}") for x in Item.objects.all()])

    try:
        itemid = forms.ChoiceField(label="Select Item Name",choices=[('','-------------------')]+[(x.id,f"{x.item_name}-{x.vendor}") for x in Item.objects.all()])
    except:
        itemid = forms.ChoiceField(choices = [('','---------------------')])
    
    received_quantity = forms.IntegerField(widget=forms.NumberInput)
    received_quantity.widget.attrs.update(
        {
            'min': 1
        }
    )



class SaleAddForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(SaleAddForm, self).__init__(*args, **kwargs)
        self.fields['itemid'] = forms.ChoiceField(label="Select Item Name",choices=[('','-------------------')]+[(x.id,f"{x.item_name} - {x.vendor}") for x in Item.objects.all()])

    try:
        itemid = forms.ChoiceField(label="Select Item Name",choices=[('','-------------------')]+[(x.id,f"{x.item_name}-{x.vendor}") for x in Item.objects.all()])
    except:
        itemid = forms.ChoiceField(choices = [('','---------------------')])
    
    sold_quantity = forms.IntegerField(widget=forms.NumberInput)
    
    sold_quantity.widget.attrs.update(
        {
            'min': 1
        }
    )

    def clean(self):
        cleaned_data = super().clean()
        itemid = cleaned_data['itemid']
        sold_quantity = cleaned_data['sold_quantity']
                
        item = Item.objects.get(pk = itemid)
        
        if(sold_quantity > item.remaining_quantity):
            raise ValidationError(f"Error!! Sale quantity cannot be greater than remaining stock qunatity for {item.item_name}.")




class CategoryAddForm(forms.Form):
    name = forms.CharField(label='Category Name', max_length=200)
    
    def clean_name(self):
        name = self.cleaned_data['name']
        try:
            Category.objects.get(category_name__iexact = name)
            raise ValidationError("Error!! Category already exists.")
        except Category.DoesNotExist:
            return name