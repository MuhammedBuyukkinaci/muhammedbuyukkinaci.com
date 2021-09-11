from django.db import models
from PIL import Image

# Create your models here.

class Image(models.Model):
    time = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.location