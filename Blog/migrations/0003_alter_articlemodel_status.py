# Generated by Django 3.2.7 on 2021-10-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_auto_20211011_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='status',
            field=models.BooleanField(default=True, verbose_name='نشان داده شود/نشود ؟'),
        ),
    ]
