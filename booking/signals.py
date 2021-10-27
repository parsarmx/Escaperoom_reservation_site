import jdatetime
from django.core.exceptions import MultipleObjectsReturned
from django.db.models.signals import post_save, pre_save
from django.core.signals import request_started
from django.dispatch import receiver
from .models import ReserveTime
from .reservation_sms import send_message_to_player, send_message_to_ESCAPEE
from jdatetime import date as jd
from .date_convertor import week_day_convert, month_convertor


@receiver([post_save, request_started], sender=ReserveTime)
def show(sender, instance, **kwargs):
    try:
        player = ReserveTime.objects.get(id=str(instance)).player.name
        # it returns time and slice the second part of time
        time = str(ReserveTime.objects.get(pk=str(instance)).time)
        phone = ReserveTime.objects.get(pk=str(instance)).player.phone
        year = ReserveTime.objects.get(pk=str(instance)).date.date.year
        month = ReserveTime.objects.get(pk=str(instance)).date.date.month
        day = ReserveTime.objects.get(pk=str(instance)).date.date.day

        # this part convert the gregorian datetime to jalali date time using year, month and day
        j_date = jd.fromgregorian(year=year, month=month, day=day)
        j_date_str = j_date.strftime('%d %m %Y')
        # this part convert the weekday and month to persian weekday using date_convertor

        j_weekday = week_day_convert(j_date.strftime('%A'))
        j_month = month_convertor(int(j_date.strftime('%-m')))
        j_day = j_date.strftime('%-d')
        print(f'player:{str(player)}\n'
              f'phone:{phone}\n'
              f'time:{time}\n'
              f'date:{str(j_date)}\n')
        # f'{j_month}\n')
        return send_message_to_player(phone, player, j_month, j_day, j_weekday, time), \
               send_message_to_ESCAPEE(phone, player, j_date_str, time)
    except AttributeError:
        return AttributeError
