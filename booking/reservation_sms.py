from ippanel import Client
from jdatetime import date as jd
from .API_CODES import SMS

api_key = SMS


def send_message_to_player(phone_number, player_name, month, date, week_day, time):
    text = f'''سلام {player_name} عزیز،
رزرو سانس {week_day} {date} {month} ساعت {time} برای شما ثبت شد!
امیدواریم توی سیاه چال بهتون خوش بگذره.
'''
    sms = Client(api_key)
    credit = sms.get_credit()
    bulk_id = sms.send(
        "5000125475",  # originator
        [phone_number],  # recipients
        text
    )
    return bulk_id


def send_message_to_ESCAPEE(phone_number, player_name, date, time):
    text = f'''رزرو سیاه چال انجام شد!
نام : {player_name}
شماره تماس : {phone_number}
تاریخ: {date}
ساعت: {time}
'''
    sms = Client(api_key)
    credit = sms.get_credit()
    bulk_id = sms.send(
        "5000125475",  # originator
        ['phone_number'],  # recipients
        text
    )
    return bulk_id
