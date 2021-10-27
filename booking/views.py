
from django.http import HttpResponse, Http404

from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
import time as t
from .models import *
from .forms import *
import datetime
from jalali_date import *
import jdatetime
import logging
import json
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
from azbankgateways.exceptions import AZBankGatewaysException

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
class home(ListView):
    model = EscapeRoom
    template_name = 'booking/home.html'


def reserve_details(request, name):
    games = EscapeRoom.objects.all().get(name=name)
    dates = ReserveDate.objects.filter(name__name=name)
    today = jdatetime.date.today()
    times = ReserveTime.objects.all()
    day_list = [(today + jdatetime.timedelta(days=x)) for x in range(8)]

    return render(request, 'booking/reserver.html',
                  {'games': games, 'day_list': day_list, 'today': today, 'dates': dates, 'times': times})



@api_view(['GET', 'POST'])
def ReservePage(request, name=None, date=None, pk=None):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    reserve_time = ReserveTime.objects.all().get(date__date=date, id=pk)
    if request.method == "GET" and not tracking_code:
        form = RegisterForm(initial={'game': EscapeRoom.objects.all().get(name=name)})
        return render(request, 'booking/information_page.html', {'form': form})

    elif request.method == "POST":
        form = RegisterForm(request.POST)


        # this field checks if a player exist ; player will choose form the existent model
        if form.is_valid() and Player.objects.all().filter(
                phone=form.cleaned_data['phone'].replace(" ", "")).count() != 0:

            e_name = str(EscapeRoom.objects.all().get(name=form.cleaned_data['game']))
            with open('booking/data_keeper.json', 'w') as file:
                file.write(json.dumps({"name": e_name,
                                       "date": date,
                                       "pk": pk,
                                       "phone": form.cleaned_data['phone'].replace(" ", "")}))
            return go_to_gateway_view(request)

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    if bank_record.is_success:
        reserve_time.status = True
        file = open("booking/data_keeper.json", "r")
        info = json.loads(file.read())
        reserve_time.player = Player.objects.all().get(phone=info['phone'])
        reserve_time.game = EscapeRoom.objects.all().get(name=info['name'])
        reserve_time.save()
        return HttpResponse('OK')


def go_to_gateway_view(request):
    # خواندن مبلغ از هر جایی که مد نظر است
    amount = 10000
    # تنظیم شماره موبایل کاربر از هر جایی که مد نظر است
    user_mobile_number = '+989353431049'  # اختیاری

    factory = bankfactories.BankFactory()
    try:
        bank = factory.create(
            bank_models.BankType.ZARINPAL)  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        file = open("booking/data_keeper.json", "r")
        info = json.loads(file.read())
        bank.set_client_callback_url(
            f"/reserve-page/{info['name']}/{info['date']}/{info['time']}/")
        file.close()
        bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # redirect to failed page.
        raise e

