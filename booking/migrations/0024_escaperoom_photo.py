# Generated by Django 3.2.7 on 2021-10-01 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0023_auto_20211001_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='escaperoom',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
