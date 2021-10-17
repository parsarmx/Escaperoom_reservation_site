from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from .slug_generate import unique_slug_generator
from django.db.models.signals import pre_save


# Create your models here.

class ArticleModelManager(models.Manager):

    def get_by_id(self, id_article):
        query = self.get_queryset().filter(id=id_article, status=True)
        if query.count() == 1:
            return query.first()
        else:
            return None


class ArticleModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان مقاله')
    img = models.ImageField(upload_to='img', verbose_name='تصویر مقاله')
    descriptions = models.TextField(verbose_name='محتوا مقاله')
    slug = models.SlugField(unique=True, blank=True, verbose_name='ادرس URL')
    creat = models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد ')
    publish = models.TimeField(default=timezone.now, verbose_name='زمان انتشار')
    update = models.TimeField(auto_now=True, verbose_name='زمان اپدیت')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نویسنده مقاله')
    status = models.BooleanField(default=True, verbose_name='نشان داده شود/نشود ؟')

    objects = ArticleModelManager()

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail_article',
                       kwargs={
                           'article_id': self.id,
                           'article_slug': self.slug
                       })


def article_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(article_pre_save_receiver, ArticleModel)
