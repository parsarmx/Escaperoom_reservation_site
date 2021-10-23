from ippanel import Client
from jdatetime import date as jd

api_key = ''


def send_message(phone_number, player_name, month, date, week_day, time):
    text = f'''سلام {player_name}  عزیز،
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
