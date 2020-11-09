from django import forms
from API.models import Category,Vendor

class ItemAddForm(forms.Form):
    item_name  = forms.CharField(label='Item Name', max_length=200)
    category = forms.ChoiceField(choices=[('','-------------------')]+[(x.id,x.category_name) for x in Category.objects.all()],required=False)
    price = forms.IntegerField(widget=forms.NumberInput)
    vendor = forms.ChoiceField(choices=[('','-------------------')]+[(x.id,x.name) for x in Vendor.objects.all()],required=False)

    price.widget.attrs.update(
        {
            'min': 0
        }
    )
   
