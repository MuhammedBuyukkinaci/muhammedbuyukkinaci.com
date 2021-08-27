from django.db import models
from datetime import datetime
# Create your models here.

# Creating a WebPage table
class Category(models.Model):
    category_title = models.CharField(max_length=40)
    category_explanation = models.CharField(max_length=200)
    category_slug = models.CharField(max_length=70)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_title

# Creating a WebPage table
class Article(models.Model):
    article_title = models.CharField(max_length=40)
    article_explanation = models.TextField()
    article_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_slug = models.CharField(max_length=70)
    article_owner = models.CharField(max_length=40)
    article_time = models.DateTimeField(default=datetime.now,blank=True, null=True)
    article_source = models.CharField(max_length=40,blank=True, null=True)

    def __str__(self):
        return self.article_title