# Generated by Django 3.2.7 on 2021-10-01 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0021_auto_20211001_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservedate',
            old_name='reserve',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='reservedate',
            old_name='status',
            new_name='reserved',
        ),
    ]
