from django.db import models

# Create your models here.

# Creating a WebPage table
class Category(models.Model):
    category_title = models.CharField(max_length=40)
    category_explanation = models.CharField(max_length=200)

    def __str__(self):
        return self.category_title

# Creating a WebPage table
class Article(models.Model):
    article_title = models.CharField(max_length=40)
    article_explanation = models.TextField()
    article_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.article_title