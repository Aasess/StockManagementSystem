from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Employee
from django.contrib.auth.hashers import make_password

# Create your views here.
def signup(request):
    if(request.method == "POST"):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #get first phone number
            phone = int(request.POST.dict()['phone'])
            password = request.POST.dict()['password1']
            #check if that number is registered or not
            employee = Employee.objects.filter(phone=phone)
            if employee.exists():
                #check if initial password is empty or not
                for emp in employee:
                    if(emp.password == ""):   
                        form.save()
                        #hash the password and save it to employee
                        emp.password = make_password(password = emp.password,salt=None,hasher='default')
                        emp.save()
                        return redirect('login')
                    else:
                        return render(request,'Account/Signup.html',{'form':form,'error_phone':"User is already registered with same phone number."})
            else:
                return render(request,'Account/Signup.html',{'form':form,'error_phone':"Phone Number is not registered."})
            
            
    else:
        form = UserCreationForm()
    return render(request,'Account/Signup.html',{'form':form})

