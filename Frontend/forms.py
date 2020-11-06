from django import forms

class ItemAddForm(forms.Form):
    category_choice = [
        ['Medicine','Medicine'],
        ['Paste','Paste'],
        ['Brush','Brush']
    ]

    stock_choices = (
        (0,'Out of Stock'),
        (1,'In Stock')
    )

    item_name  = forms.CharField(label='Item Name', max_length=200)
    item_name = models.CharField(max_length=200)
    category = forms.ChoiceField(choices = category_choice)
    price = models.FloatField(default=0)
    price = forms.FloatField()
    vendor = forms.IntegerField
    remaining_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length = 200,blank=True)
    is_stock = models.IntegerField(choices = stock_choices)
