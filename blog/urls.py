from django.urls import path
from .views import *
from django.urls import re_path
from django.views.generic.base import RedirectView
from django.shortcuts import reverse
app_name = "blog"

urlpatterns = [
    path('',BlogCategoriesView.as_view(), name = 'blog'),
    path('<slug:category_slug>/', BlogArticlesView.as_view(), name='filtered_category'),
    path('<slug:category_slug>', BlogArticlesView.as_view(), name='filtered_category_wo_slash'),
    path('<slug:category_slug>/<int:pk>/', ArticleView.as_view(), name='article'),
    path('<slug:category_slug>/<int:pk>', ArticleView.as_view(), name='article_wo_slash'),
    re_path(r'^.*$', RedirectView.as_view(url = '/blog/',permanent=False), name='blogredirector'),
]

