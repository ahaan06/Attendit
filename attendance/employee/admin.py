from django.contrib import admin
from .models import Employee,EmployeeLog

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','dob')

@admin.register(EmployeeLog)
class EmployeeLogAdmin(admin.ModelAdmin):
    list_display = ('employee','starttime','endtime','date')    