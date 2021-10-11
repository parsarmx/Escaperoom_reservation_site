from django.contrib import admin
from .models import ArticleModel

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'publish', 'status']
    search_fields = ["title", 'author']
    list_filter = ['author']
    list_editable = ['status']

admin.site.register(ArticleModel, ArticleModelAdmin)


