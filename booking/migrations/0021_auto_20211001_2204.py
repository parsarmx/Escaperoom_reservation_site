# Generated by Django 3.2.7 on 2021-10-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0020_alter_reservedate_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservedate',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='reservedate',
            name='date',
            field=models.DateField(),
        ),
    ]
