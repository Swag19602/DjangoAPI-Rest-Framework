from operator import mod
from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=500)
    emp_code=models.CharField(max_length=3)
    mobile=models.CharField(max_length=15)