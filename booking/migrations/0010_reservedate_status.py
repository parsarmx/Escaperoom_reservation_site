# Generated by Django 3.2.7 on 2021-10-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_delete_ok'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservedate',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
