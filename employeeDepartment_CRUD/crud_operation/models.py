from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=300)
    salary=models.IntegerField()
    departmentId=models.ForeignKey(
        "Department", on_delete=models.CASCADE)
    managerId=models.IntegerField()

class Department(models.Model):
    DepartmentId=models.IntegerField(primary_key=True)
    departmentName=models.CharField(max_length=400)
