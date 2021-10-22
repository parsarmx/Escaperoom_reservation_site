from django.db.models.signals import post_save, pre_save
from django.core.signals import request_started
from django.dispatch import receiver
from .models import ReserveTime
from .reservation_sms import send_message


@receiver([post_save, request_started], sender=ReserveTime)
def show(sender, instance, **kwargs):
    player = ReserveTime.objects.get(time=str(instance)).player
    time = ReserveTime.objects.get(time=str(instance))
    phone = ReserveTime.objects.get(time=str(instance)).player.phone
    date = ReserveTime.objects.get(time=str(instance)).date
    print(f'player: {player},\n phone: {phone},\ntime:{time}, \n date: {date}')
    return send_message(phone, player, date, time)
