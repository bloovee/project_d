# Generated by Django 4.1.7 on 2023-03-30 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_learning', '0007_personalinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='LearningCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('course_level', models.CharField(choices=[('B', 'Basic'), ('I', 'Intermediate'), ('A', 'Advanced')], max_length=1)),
                ('employee', models.ManyToManyField(to='employee_learning.employee')),
            ],
        ),
    ]
