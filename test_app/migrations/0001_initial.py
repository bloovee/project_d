# Generated by Django 4.1.7 on 2023-03-20 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages='max 10 letters', help_text='test text', max_length=10)),
                ('select_1', models.CharField(max_length=10)),
                ('boolean', models.BooleanField()),
                ('date', models.DateField(blank=True)),
                ('integer', models.IntegerField()),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ForeignTestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_2', models.CharField(max_length=5, verbose_name='Foreign Key Test')),
                ('foreign_test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_app.testmodel')),
            ],
        ),
    ]
