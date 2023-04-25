# Generated by Django 4.1.7 on 2023-03-30 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_learning', '0004_employee_priority_alter_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='reg_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Data Registration Date'),
        ),
    ]