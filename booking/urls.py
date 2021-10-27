from azbankgateways.urls import az_bank_gateways_urls
from django.urls import path
from .views import *
from django.conf.urls.static import static

urlpatterns = [

    path('home/', home.as_view()),
    path('reserve/<str:name>', reserve_details, name='reserve'),

    path('reserve-page/<name>/<date>/<int:pk>/', ReservePage, name='reserve-page'),
    path('bankgateways/', az_bank_gateways_urls()),
    # path('go-to-gateway/', go_to_gateway_view, name='go_to_gateway'),
    # path('callback-gateway/<name>/<date>/<time>/', callback_gateway_view, name='callback-gateway')
]
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

