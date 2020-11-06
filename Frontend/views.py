from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url='/account/login/')
def home(request):
    return render(request,'Frontend/home.html',{'error':False})