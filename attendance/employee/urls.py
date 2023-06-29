from django.urls import path
from .views import employee_logs

urlpatterns = [
    path('logs', employee_logs, name='logs'),
   path('employee/<int:employee_id>/logs/', employee_logs, name='employee_logs'),
]