from django.contrib import admin

# Register your models here.
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    
    #Which fields to show on admin page before changing
    list_display = ("time", "location",)

admin.site.register(Image,ImageAdmin)
