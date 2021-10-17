from jdatetime import date as jd
from django.db import models
from jalali_date import *
from django_jalali.db import models as jmodels
import datetime


# EscapeRoom model
class EscapeRoom(models.Model):
    city_choices = (
        ('K', 'Karaj'),
        ('T', 'Tehran')
    )

    name = models.CharField(max_length=50)
    time = models.IntegerField()
    price = models.IntegerField()
    description = models.TextField()
    story = models.TextField()
    city = models.CharField(max_length=1, choices=city_choices)
    hardship = models.IntegerField(null=True)
    age = models.IntegerField()
    genre = models.CharField(max_length=20)
    photo = models.ImageField(null=True, blank=True, upload_to='static/booking/images/')
    # location =
    def __str__(self):
        return f'{self.name}'


class Player(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number_of_players = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    game = models.ForeignKey(EscapeRoom, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}, {self.last_name}'


class ReserveDate(models.Model):
    date = models.DateField()
    name = models.ForeignKey(EscapeRoom, on_delete=models.CASCADE, null=True)

    def j_date(self):
        return date2jalali(self.date)

    def jd_create_datetime(self):
        return jd.fromgregorian(year=self.date.year, month=self.date.month, day=self.date.day)

    def __str__(self):
        return f'{self.date} {self.name}'


class ReserveTime(models.Model):
    TIME_CHOICES = (
        (datetime.time(12, 00), '12:00'), (datetime.time(12, 15), '12:15'), (datetime.time(12, 30), '12:30'),
        (datetime.time(12, 45), '12:45'), (datetime.time(13, 00), '13:00'), (datetime.time(13, 15), '13:15'),
        (datetime.time(13, 30), '13:30'), (datetime.time(13, 45), '13:45'), (datetime.time(14, 00), '14:00'),
        (datetime.time(14, 15), '14:15'), (datetime.time(14, 30), '13:30'), (datetime.time(14, 45), '14:45'),
        (datetime.time(15, 00), '15:00'), (datetime.time(15, 15), '15:15'), (datetime.time(15, 45), '15:45'),
        (datetime.time(16, 00), '16:00'), (datetime.time(16, 15), '16:15'), (datetime.time(16, 30), '16:45'),
        (datetime.time(17, 00), '17:00'), (datetime.time(17, 15), '17:15'), (datetime.time(17, 30), '17:30'),

    )

    time = models.TimeField(choices=TIME_CHOICES)
    date = models.ForeignKey(ReserveDate, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)
    game = models.ForeignKey(EscapeRoom, on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.time} {self.date}'
