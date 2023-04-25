import datetime
from django.db import models

# Create your models here.

CHOICES = [
    ('red','red light'),
    ('blue', 'blue light'),
    ('yellow','yellow light'),
]

COLOR = [
    ('R', 'Red'),
    ('G', 'Green'),
    ('B', 'Blue'),
]

class ColorChoice(models.Model):
    color = models.CharField(max_length=1, choices=COLOR)

class TestModel(models.Model):
    name = models.CharField(max_length=10,help_text="test text",error_messages="max 10 letters")
    select_1 = models.CharField(max_length=10)
    boolean = models.BooleanField()
    date = models.DateField(blank=True, default=datetime.date.today)
    boolean_2 = models.BooleanField(default=True)
    color = models.CharField(max_length=20, choices=CHOICES)

class ForeignTestModel(models.Model):
    id = models.AutoField
    name_2 = models.CharField(max_length=5, verbose_name="Foreign Key Test")
    foreign_test = models.ForeignKey(TestModel, on_delete=models.CASCADE)