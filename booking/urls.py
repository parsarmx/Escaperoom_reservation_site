from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [

    path('home/', home.as_view()),
    path('reserve/<str:name>', reserve_details, name='reserve'),
    path('reserve/<str:name>/<str:time>', reserve_page.as_view(), name='reserve_page')
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
