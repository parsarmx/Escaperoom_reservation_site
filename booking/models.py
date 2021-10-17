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
    number_of_players = models.IntegerField()
    city = models.CharField(max_length=1, choices=city_choices)
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

    def j_date(self):
        return date2jalali(self.date)

    def jd_create_datetime(self):
        return jd.fromgregorian(year=self.date.year, month=self.date.month, day=self.date.day)

    activate = models.BooleanField(default=False)
    reserved = models.BooleanField(default=False)
    name = models.ForeignKey(EscapeRoom, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.date}'


class ReserveTime(models.Model):
    time = models.TimeField()
    date = models.ForeignKey(ReserveDate, on_delete=models.CASCADE)
