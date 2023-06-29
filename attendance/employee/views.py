#from django.shortcuts import render#

# Create your views here.
from datetime import datetime, time

from datetime import  time, timedelta, datetime

from django.shortcuts import render 

from .models import Employee, EmployeeLog 


def calculate_overtime_pay(employee):
    x= EmployeeLog.objects.filter(employee=employee) 
    import ipdb
    ipdb.set_trace()
    start_time = EmployeeLog.start_time.time()
    end_time = EmployeeLog.end_time.time()

    regular_start_time = time(hour=8, minute=30)
    regular_end_time = time(hour=17, minute=30)

    if start_time < regular_start_time:
        start_time = regular_start_time
    if end_time > regular_end_time:
        end_time = regular_end_time

    duration = datetime.combine(EmployeeLog.date, end_time) - datetime.combine(EmployeeLog.date, start_time)
    overtime = max(duration - timedelta(hours=EmployeeLog.Employee.regular_working_hours), timedelta())

    overtime_pay = overtime.total_seconds() / 3600 * EmployeeLog.Employee.overtime_rate

    return overtime_pay


def employee_logs(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    logs = EmployeeLog.objects.filter(employee=employee).order_by('date')

    regular_pay = employee.monthly_salary / 30  # Assuming 30 days in a month

   
    total_pay = 0
    pay_details = []
    current_month = None

    for log in logs:
        overtime_pay = calculate_overtime_pay(log)
        daily_pay = regular_pay + overtime_pay

        if log.date.month != current_month:
            current_month = log.date.month
            total_pay = employee.monthly_salary  # Reset total pay to monthly salary

        total_pay += daily_pay  # Add daily pay to the total

        pay_details.append({
            'date': log.date,
            'daily_pay': daily_pay,
            'total_pay': total_pay
        })

    context = {
        'employee': employee,
        'pay_details': pay_details
    }
    return render(request, 'index.html', context)
