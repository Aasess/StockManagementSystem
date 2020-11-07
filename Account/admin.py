from django.contrib import admin
from .models import Employee

# Register your models here.
# admin.site.register(Employee)


class employee_admin(admin.ModelAdmin):
    list_display =  ('first_name', 'last_name', 'phone', 'address')

admin.site.register(Employee, employee_admin)
