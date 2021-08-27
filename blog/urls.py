from django.urls import path
from .views import *

app_name = "blog"

urlpatterns = [
    path('',BlogCategoriesView.as_view(), name = 'blog'),
    path('<slug:category_slug>/', BlogArticlesView.as_view(), name='filtered_category'),
    path('<slug:category_slug>/<int:pk>/', ArticleView.as_view(), name='article'),
]

