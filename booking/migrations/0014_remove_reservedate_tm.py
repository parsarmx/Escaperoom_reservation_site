# Generated by Django 3.2.7 on 2021-10-01 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_reservedate_tm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservedate',
            name='tm',
        ),
    ]
