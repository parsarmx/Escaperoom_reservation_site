from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView

from .models import *
from .forms import *
import datetime
from jalali_date import *
import jdatetime


# Create your views here.
class home(ListView):
    model = EscapeRoom
    template_name = 'booking/index.html'


def reserve_details(request, name):
    games = EscapeRoom.objects.all().get(name=name)
    dates = ReserveDate.objects.all()
    today = jdatetime.date.today()
    times = ReserveTime.objects.all()
    day_list = [(today + jdatetime.timedelta(days=x)) for x in range(8)]

    return render(request, 'booking/reserver.html',
                  {'games': games, 'day_list': day_list, 'today': today, 'date': dates, 'times': times})


class reserve_page(FormView):
    template_name = 'booking/reserve_page.html'
    form_class = RegisterForm
    success_url = '/thanks/'
