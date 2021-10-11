from django.views.generic import ListView
from django.shortcuts import render
from .models import ArticleModel


# Create your views here.


class List_article(ListView):
    template_name = 'blog/list_article.html'
    paginate_by = 6

    def get_queryset(self):
        return ArticleModel.objects.filter(status=True)
