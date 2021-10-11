# Generated by Django 3.2.7 on 2021-10-11 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlemodel',
            name='creat',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد '),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='publish',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='articlemodel',
            name='update',
            field=models.TimeField(auto_now=True, verbose_name='زمان اپدیت'),
        ),
    ]
