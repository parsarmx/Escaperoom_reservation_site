# Generated by Django 3.2.7 on 2021-10-03 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0026_alter_escaperoom_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservedate',
            name='time',
        ),
        migrations.AlterField(
            model_name='escaperoom',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='static/booking/images/'),
        ),
        migrations.CreateModel(
            name='ReserveTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.reservedate')),
            ],
        ),
    ]
