from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
# Create your views here.
def signup(request):
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #get first phone number
            phone = int(request.POST.dict()['phone'])
            #check if that number is registered or not
            employee = Employee.objects.filter(phone=phone)
            if employee.exists():
                form.save()
                return redirect('login')
            else:
                return render(request,'Account/Signup.html',{'form':form,'error_phone':"Phone Number is not registered."})
            
            
    else:
        form = UserCreationForm()
    return render(request,'Account/Signup.html',{'form':form})


def login(request):
    return render(request,'Account/Login.html')