import jdatetime
from django.core.exceptions import MultipleObjectsReturned
from django.db.models.signals import post_save, pre_save
from django.core.signals import request_started
from django.dispatch import receiver
from .models import ReserveTime
from .reservation_sms import send_message
from jdatetime import date as jd
from .date_convertor import week_day_convert, month_convertor


@receiver([post_save, request_started], sender=ReserveTime)
def show(sender, instance, **kwargs):
    try:
        player = ReserveTime.objects.get(time=str(instance)).player.name
        time = ReserveTime.objects.get(time=str(instance))
        phone = ReserveTime.objects.get(time=str(instance)).player.phone
        year = ReserveTime.objects.get(time=str(instance)).date.date.year
        month = ReserveTime.objects.get(time=str(instance)).date.date.month
        day = ReserveTime.objects.get(time=str(instance)).date.date.day

        # this part convert the gregorian datetime to jalali date time using year, month and day
        j_date = jd.fromgregorian(year=year, month=month, day=day)

        # this part convert the weekday and month to persian weekday using date_convertor
        j_weekday = week_day_convert(j_date.strftime('%A'))
        j_month = month_convertor(j_date.strftime('%-m'))
        j_day = j_date.strftime('%-d')

        print(f'player:{str(player)}\nphone:{phone}\ntime:{time}\ndate:{str(j_date)}')
        return send_message(phone, player, j_month, j_day, j_weekday, time)
    except AttributeError:
        print('except')
