from django import forms
from API.models import Category

class ItemAddForm(forms.Form):
    
    category_choice = [
        ('','Not Specified'),
        ('Medicine','Medicine'),
        ('Paste','Paste'),
        ('Brush','Brush')
    ]

    item_name  = forms.CharField(label='Item Name', max_length=200)
    category = forms.ChoiceField(choices = category_choice)
    price = forms.IntegerField(widget=forms.NumberInput)
    vendor = forms.IntegerField()

    price.widget.attrs.update(
        {
            'min': 0
        }
    )
   