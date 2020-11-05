from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    phone = models.CharField(max_length = 15)
    address = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200,blank=True)


    def __str__(self):
        return self.first_name +" "+ self.last_name