# Generated by Django 4.2.2 on 2023-06-28 06:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyWage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('date_of_joining', models.DateField()),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('number_of_hours', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('overtime_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('regular_working_hours', models.DecimalField(decimal_places=1, max_digits=3)),
                ('monthly_salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
            bases=('user.user',),
        ),
        migrations.CreateModel(
            name='EmployeeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employee.employee')),
            ],
        ),
    ]
