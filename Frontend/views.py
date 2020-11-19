from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import ItemAddForm,VendorAddForm,StockAddForm,SaleAddForm,CategoryAddForm
from django.http import JsonResponse
from django.template.loader import render_to_string
import requests
from django.contrib.auth.models import User
from .token_generator import access_token_generate
from StockManagementSystem.settings import WEBSITE_URL

@login_required(login_url='/account/login/')
def home(request):
    req = requests.get(url = f'{WEBSITE_URL}/api/item/',headers = access_token_generate())
    result = req.json()
    return render(request,'Frontend/Item.html',{'items':result['data']})


@login_required(login_url='/account/login/')
def item_add(request):
    if request.method == "POST":
        form = ItemAddForm(request.POST)
       
        if form.is_valid():
            itemname = form.cleaned_data['item_name']
            categoryid = form.cleaned_data['category']
            vendorid = form.cleaned_data['vendor']
            price = form.cleaned_data['price']
            
            data = {
                'item_name':itemname,
                'price':int(price),
                'category':categoryid,
                'vendor':vendorid,
                'created_by':str(request.user),
            }

            requests.post(url = f'{WEBSITE_URL}/api/item/',headers = access_token_generate(),data = data)
            form = ItemAddForm()
            return render(request,'Frontend/ItemAdd.html',{'form':form,'success':f'The item - {itemname} is added successfully.'})
        
    else:
        form = ItemAddForm()
    
    return render(request,'Frontend/ItemAdd.html',{'form':form})


@login_required(login_url='/account/login/')
def vendor(request):
    req = requests.get(url = f'{WEBSITE_URL}/api/vendor/',headers = access_token_generate())
    result = req.json()
    return render(request,'Frontend/Vendor.html',{'vendors':result['data']})



@login_required(login_url='/account/login/')
def vendor_add(request):
    if request.method == "POST":
        form = VendorAddForm(request.POST)
       
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            
            data = {
                'name':name,
                'address':address,
                'phone':phone,
                'created_by':str(request.user),
            }

            requests.post(url = f'{WEBSITE_URL}/api/vendor/',headers = access_token_generate(),data = data)
            form = VendorAddForm()
            return render(request,'Frontend/VendorAdd.html',{'form':form,'success':f'The vendor - {name} is added successfully.'})
        
    else:
        form = VendorAddForm()
    
    return render(request,'Frontend/VendorAdd.html',{'form':form})



@login_required(login_url='/account/login/')
def sale(request):
    req = requests.get(url = f'{WEBSITE_URL}/api/sale/',headers = access_token_generate())
    result = req.json()
    return render(request,'Frontend/Sale.html',{'sales':result['data']})


@login_required(login_url='/account/login/')
def sale_add(request):
    if request.method == "POST":
        form = SaleAddForm(request.POST)
       
        if form.is_valid():
            itemid = form.cleaned_data['itemid']
            sold_quantity = form.cleaned_data['sold_quantity']
            
            data = {
                'item':itemid,
                'sold_quantity':int(sold_quantity),
                'created_by':str(request.user),
            }
            requests.post(url = f'{WEBSITE_URL}/api/sale/',headers = access_token_generate(),data = data)
            form = SaleAddForm()
            return render(request,'Frontend/SaleAdd.html',{'form':form,'success':f'The sold quantity - {sold_quantity} is added successfully.'})
        
    else:
        form = SaleAddForm()
    
    return render(request,'Frontend/SaleAdd.html',{'form':form})



@login_required(login_url='/account/login/')
def stock(request):
    req = requests.get(url = f'{WEBSITE_URL}/api/stock/',headers = access_token_generate())
    result = req.json()
    return render(request,'Frontend/Stock.html',{'stocks':result['data']})



@login_required(login_url='/account/login/')
def stock_add(request):
    if request.method == "POST":
        form = StockAddForm(request.POST)
       
        if form.is_valid():
            itemid = form.cleaned_data['itemid']
            received_quantity = form.cleaned_data['received_quantity']
            
            data = {
                'item':itemid,
                'recieved_quantity':int(received_quantity),
                'created_by':str(request.user),
            }
            requests.post(url = f'{WEBSITE_URL}/api/stock/',headers = access_token_generate(),data = data)
            form = StockAddForm()
            return render(request,'Frontend/StockAdd.html',{'form':form,'success':f'The received quantity - {received_quantity} is added successfully.'})
        
    else:
        form = StockAddForm()
    
    return render(request,'Frontend/StockAdd.html',{'form':form})




@login_required(login_url='/account/login/')
def category_add(request):
    if request.method == "POST":
        form = CategoryAddForm(request.POST)
       
        if form.is_valid():
            category_name = form.cleaned_data['name']
            
            data = {
                'category_name':category_name
            }
            requests.post(url = f'{WEBSITE_URL}/api/category/',headers = access_token_generate(),data = data)
            form = CategoryAddForm()
            return render(request,'Frontend/CategoryAdd.html',{'form':form,'success':f'The category - {category_name} is added successfully.'})
        
    else:
        form = CategoryAddForm()
    return render(request,'Frontend/CategoryAdd.html',{'form':form})


@login_required(login_url="/acccount/login/")
def stock_add_direct(request):
    itemid = request.POST.get("modal_itemid")
    received_quantity = request.POST.get("modal_receiveqty")
    data = {
            'item':itemid,
            'recieved_quantity':int(received_quantity),
            'created_by':str(request.user),
        }
    requests.post(url = f'{WEBSITE_URL}/api/stock/',headers = access_token_generate(),data = data)
    return redirect('home')



@login_required(login_url="/acccount/login/")
def sale_add_direct(request):
    itemid = request.POST.get("modal_itemid")
    sold_quantity = request.POST.get("modal_soldqty")
    data = {
            'item':itemid,
            'sold_quantity':int(sold_quantity),
            'created_by':str(request.user),
        }
    requests.post(url = f'{WEBSITE_URL}/api/sale/',headers = access_token_generate(),data = data)
    return redirect('home')