from rest_framework import viewsets
from . import models
from . import serializer

class EmpoloyeeViewset(viewsets.ModelViewSet):
    queryset=models.Employee.objects.all()
    serializer_class=serializer.EmployeeSerializer

# list () , retrieve(), create() ,update(), destroy()