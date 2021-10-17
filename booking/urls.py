from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [

    path('home/', home.as_view()),
    path('reserve/<str:name>', reserve_details, name='reserve'),
    path('reserve/<str:name>/<str:date>/<str:time>', ReservePage, name='reserve_page')
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
