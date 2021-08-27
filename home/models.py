from django.db import models

# Welcome Page Text
class Homepage(models.Model):

    home_summary = models.CharField(max_length=50)
    home_text = models.TextField()

    def __str__(self):
        return self.home_summary