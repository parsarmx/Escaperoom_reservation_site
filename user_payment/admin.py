from django.contrib import admin
from .models import PrePayment


# Register your models here.
@admin.register(PrePayment)
class EscapeAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'date',
        'time_id',
        'phone',
    ]
