from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(EscapeRoom)
class EscapeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'time',
        'price',
        'description',
        'story',
        'city',
        'age',
        'genre',

    ]


@admin.register(ReserveDate)
class DateAdmin(admin.ModelAdmin):
    list_display = [
        'j_date',
        'name',
    ]


@admin.register(Player)
class Player(admin.ModelAdmin):
    list_display = [
        'name',
        'last_name',
        'number_of_players',
        'email',
        'phone'
    ]


@admin.register(ReserveTime)
class Time(admin.ModelAdmin):
    list_display = [
        'time',
        'date',
        'player',
        'game',
        'status'
    ]
