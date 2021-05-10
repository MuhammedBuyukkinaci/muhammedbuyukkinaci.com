from django.contrib import admin

# Register your models here.
from .models import Skill,Page
admin.site.register(Skill)
admin.site.register(Page)