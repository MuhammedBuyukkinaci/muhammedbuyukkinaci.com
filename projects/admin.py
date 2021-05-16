from django.contrib import admin

# Register your models here.
from .models import Project,Detail
admin.site.register(Project)
admin.site.register(Detail)