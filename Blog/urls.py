from django.urls import path
from .views import (
    List_article,
    Detail_article,
)

app_name = 'blog'
urlpatterns = [
    path('', List_article.as_view(), name='list_article'),
    path('<int:article_id>/<str:article_slug>', Detail_article, name='detail_article')
]
