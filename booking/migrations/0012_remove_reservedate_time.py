# Generated by Django 3.2.7 on 2021-10-01 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0011_auto_20211001_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservedate',
            name='time',
        ),
    ]
