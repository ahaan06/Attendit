from django.contrib import admin
from .models import Employee,EmployeeLog,DailyWage

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','dob') 
    def save_model(self, request, obj, form, change):

        obj.set_password(obj.password)

        super(EmployeeAdmin, self).save_model(request, obj, form, change)

@admin.register(EmployeeLog)
class EmployeeLogAdmin(admin.ModelAdmin):
    list_display = ('employee','start_time','end_time','date')    

@admin.register(DailyWage)
class DailyWage(admin.ModelAdmin):
  list_display=('name','date_of_joining','hourly_rate','number_of_hours')

# Register your models here.

# @admin.register(Agent)

# class AgentAdmin(admin.ModelAdmin):

#     list_display = (

#         'email',

#         'phone',

#         'current_level',

#         'date_joined',

#         'uuid',

#         'verified',

#     )  




#     exclude = ('user_permissions','groups','last_login','is_superuser','is_staff')




#     #def save_model(self, request, obj, form, change):#

#         obj.set_password(obj.password)

#         super(AgentAdmin, self).save_model(request, obj, form, change)


