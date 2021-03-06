# Generated by Django 3.2.7 on 2021-10-17 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0031_auto_20211017_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservetime',
            name='time',
            field=models.TimeField(choices=[(datetime.time(12, 0), '12:00'), (datetime.time(12, 15), '12:15'), (datetime.time(12, 30), '12:30'), (datetime.time(12, 45), '12:45'), (datetime.time(13, 0), '13:00'), (datetime.time(13, 15), '13:15'), (datetime.time(13, 30), '13:30'), (datetime.time(13, 45), '13:45'), (datetime.time(14, 0), '14:00'), (datetime.time(14, 15), '14:15'), (datetime.time(14, 30), '13:30'), (datetime.time(14, 45), '14:45'), (datetime.time(15, 0), '15:00'), (datetime.time(15, 15), '15:15'), (datetime.time(15, 45), '15:45'), (datetime.time(16, 0), '16:00'), (datetime.time(16, 15), '16:15'), (datetime.time(16, 30), '16:45'), (datetime.time(17, 0), '17:00'), (datetime.time(17, 15), '17:15'), (datetime.time(17, 30), '17:30')]),
        ),
    ]
