from django.urls import path
from .views import List_article

app_name = 'blog'
urlpatterns = [
    path('',List_article.as_view(),name='list_article')
]
