from django.db import models
from PIL import Image
from django.utils.html import mark_safe

# Create your models here.

class Image(models.Model):
    time = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')

    @property
    def thumbnail_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.image.url))
        return ""

    def __str__(self):
        return self.location