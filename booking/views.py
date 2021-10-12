from django.shortcuts import render
from django.views import View
from .models import *
import datetime
from jalali_date import *
import jdatetime


# Create your views here.
class home(View):
    def get(self, request):
        games = EscapeRoom.objects.all()
        return render(request, 'booking/index.html', {'games': games})


class reserve(View):
    def get(self, request, name):
        games = EscapeRoom.objects.all().get(name=name)
        dates = ReserveDate.objects.all()
        today = jdatetime.date.today()
        times = ReserveTime.objects.all()
        day_list = [(today + jdatetime.timedelta(days=x)) for x in range(8)]

        return render(request, 'booking/reserver.html',
                      {'games': games, 'day_list': day_list, 'today': today, 'date': dates, 'times': times})
