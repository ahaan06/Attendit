from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    dob = models.DateField()


class EmployeeLog(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    starttime=models.TimeField()
    endtime=models.TimeField()
    date=models.DateField()