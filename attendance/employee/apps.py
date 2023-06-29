from django.apps import AppConfig


class EmployeeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'employee'

class DailyWageconfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    name='DailyWage'