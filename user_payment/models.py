from django.db import models


class PrePayment(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    time_id = models.IntegerField()
    phone = models.CharField(max_length=15, default=None)

    class Meta:
        get_latest_by = ['name']