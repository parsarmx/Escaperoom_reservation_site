# Generated by Django 3.2.7 on 2021-10-17 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0029_player_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservedate',
            name='activate',
        ),
        migrations.RemoveField(
            model_name='reservedate',
            name='player',
        ),
        migrations.RemoveField(
            model_name='reservedate',
            name='reserved',
        ),
    ]
