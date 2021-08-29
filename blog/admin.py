from django.contrib import admin
from .models import Category, Article
# Register your models here.
from tinymce.widgets import TinyMCE

from django.db import models



class ArticleAdmin(admin.ModelAdmin):
    
    #Which fields to show on admin page before changing
    list_display = ("article_title", "article_category",)
    # A search bar to search input on the below area
    search_fields = ("article_explanation",)
    # Filter options shown in the right section
    list_filter = ("article_category", )

    fieldsets = [("Main",{"fields":["article_title","article_explanation","article_category","article_slug","article_owner"]}),
    ("Subsidiary",{"fields":["article_time","article_source"]})
    ]

    # Under ArticleAdmin class
    formfield_overrides = {
        models.TextField: {'widget':TinyMCE()}
    }
    


admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)

