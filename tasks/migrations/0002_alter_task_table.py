# Generated by Django 5.0.6 on 2024-06-01 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='task',
            table='task_list',
        ),
    ]