from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/account/login/')
def home(request):
    return render(request,'Frontend/Home.html')


@login_required(login_url='/account/login/')
def item(request):
    return render(request,'Frontend/Item.html')


@login_required(login_url='/account/login/')
def vendor(request):
    return render(request,'Frontend/Vendor.html')


@login_required(login_url='/account/login/')
def sale(request):
    return render(request,'Frontend/Sale.html')


@login_required(login_url='/account/login/')
def stock(request):
    return render(request,'Frontend/Stock.html')
