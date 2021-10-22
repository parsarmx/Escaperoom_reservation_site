from kavenegar import *
from .models import *


def send_message(phone_number, player_name, date, time):
    try:
        api = KavenegarAPI('Token...')
        params = {
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'''رزرو انجام شد!
نام بازیکن: {player_name}
تاریخ : {date}
ساعت : {time}
''',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
