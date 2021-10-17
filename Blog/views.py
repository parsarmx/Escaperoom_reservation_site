from django.views.generic import ListView
from django.shortcuts import render
from .models import ArticleModel


# Create your views here.


class List_article(ListView):
    template_name = 'blog/list_article.html'
    paginate_by = 6

    def get_queryset(self):
        return ArticleModel.objects.filter(status=True)


def Detail_article(request,article_id,article_slug):
    article_view = ArticleModel.objects.get_by_id(id_article=article_id)
    context = {
        'article':article_view
    }

    return render(request,'blog/detail_article.html',context)