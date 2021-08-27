from django.contrib import admin
from .models import Category, Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):

    fieldsets = [("Main",{"fields":["article_title","article_explanation","article_category","article_slug","article_owner"]}),
    ("Subsidiary",{"fields":["article_time","article_source"]})
    ]


admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)

