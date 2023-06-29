from django.db import models
from user.models import User

class Employee(User):
   # emp=models.ForeignKey(on_delete=models.DO_NOTHING)#
    name = models.CharField(max_length=30)
    dob = models.DateField()
    overtime_rate = models.DecimalField(max_digits=4, decimal_places=2)
    regular_working_hours = models.DecimalField(max_digits=3, decimal_places=1)
    monthly_salary = models.DecimalField(max_digits=10, decimal_places=2)

class DailyWage(models.Model):
    name=models.CharField(max_length=30)
    date_of_joining=models.DateField()
    hourly_rate=models.DecimalField(max_digits=10, decimal_places=2)
    number_of_hours=models.DecimalField(max_digits=3, decimal_places=2)
    
class EmployeeLog(models.Model):
    employee=models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    start_time=models.TimeField()
    end_time=models.TimeField()
    date=models.DateField()
    
    