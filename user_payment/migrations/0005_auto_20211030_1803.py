# Generated by Django 3.2.7 on 2021-10-30 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_payment', '0004_alter_prepayment_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prepayment',
            options={'get_latest_by': ['name']},
        ),
        migrations.RemoveField(
            model_name='prepayment',
            name='time',
        ),
    ]