from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home.as_view()),
    path('reserve/<str:name>', reserve.as_view(), name='reserve')
]