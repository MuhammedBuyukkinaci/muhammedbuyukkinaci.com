from django.db import models

# Create your models here.

# Creating a Skill table
class Skill(models.Model):
    skill_name = models.CharField(max_length=30)
    skill_percent = models.IntegerField(default=20)

    def __str__(self):
        return self.skill_name

# Creating a WebPage table
class Page(models.Model):
    page_link = models.CharField(max_length=100)
    page_fontawesomeclass = models.CharField(max_length=50)
    page_color = models.CharField(max_length=10)
    page_name = models.CharField(max_length=20)

    socialmedia = 'socialmedia'
    business = 'business'
    chioces = [
        (socialmedia, 'socialmedia'),
        (business, 'business'),
    ]
    page_category = models.CharField(
        max_length=20,
        choices=chioces,
        default=socialmedia,
    )

    def __str__(self):
        return self.page_name