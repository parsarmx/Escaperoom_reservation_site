# Generated by Django 3.2.7 on 2021-10-17 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0033_auto_20211017_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='escaperoom',
            name='hardship',
            field=models.IntegerField(null=True),
        ),
    ]