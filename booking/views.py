from django.http import HttpResponse
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


def ReservePage(request, name, date, time):
    if request.method == "GET":
        form = RegisterForm(initial={'game': EscapeRoom.objects.all().get(name=name)})
        reserve_time = ReserveTime.objects.all().get(date__date=date, time=time)
        return render(request, 'booking/information_page.html', {'form': form})

    # this field will post the form

    if request.method == "POST":
        form = RegisterForm(request.POST)
        reserve_time = ReserveTime.objects.all().get(date__date=date, time=time)

        # this field checks if a player exist ; player will choose form the existent model
        if form.is_valid() and Player.objects.all().filter(phone=form.cleaned_data['phone']).count() != 0:
            reserve_time.status = True
            reserve_time.player = reserve_time.player = Player.objects.all().get(phone=form.cleaned_data['phone'])

            reserve_time.game = EscapeRoom.objects.all().get(name=name)
            reserve_time.save()

            return HttpResponse('رزرو شما انجام داده شد(2)')
        # this field create a player model if player dose not exist
        elif form.is_valid() and (reserve_time.status is False) and (Player.objects.all().filter(
                phone=form.cleaned_data['phone']).count() == 0):
            form.save()
            reserve_time.status = True
            reserve_time.player = Player.objects.all().get(phone=form.cleaned_data['phone'],
                                                           email=form.cleaned_data['email'])
            reserve_time.game = EscapeRoom.objects.all().get(name=name)
            reserve_time.save()
            return HttpResponse('رزرو شما انجام داده شد(1)')

        # this part shows if a player wants to reserve a time that dose not available
        else:
            return HttpResponse('<h1>Failed</h1>')
