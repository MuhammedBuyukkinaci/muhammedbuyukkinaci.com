from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('',BlogCategoriesView.as_view(), name = 'blog'),
]
