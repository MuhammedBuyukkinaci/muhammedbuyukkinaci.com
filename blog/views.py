from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Category, Article
from django.shortcuts import reverse,redirect
from django.http import Http404

# Create your views here.

class BlogCategoriesView(ListView):
    template_name = "blog/blog_categories.html"
    queryset = Category.objects.all()
    context_object_name = "categories"

    def get_queryset(self):
        qs = super().get_queryset().order_by('id')
        return qs

class BlogArticlesView(ListView):
    template_name = "blog/blog_articles.html"
    queryset = Article.objects.all()
    context_object_name = "articles"

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug', None)
        qs = Article.objects.filter(article_category__category_slug=category_slug)
        return qs

    def dispatch(self, *args, **kwargs):
        if len(self.get_queryset()) >0:
            return super().dispatch(*args, **kwargs)
        else:
            return redirect('blog:blog')
    
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['details'] = Detail.objects.all().order_by('detail_number')
    #     return data

class ArticleView(DetailView):

    
    template_name = "blog/article_detail.html"

    model = Article
    
    def get_queryset(self):
        qs = super().get_queryset()
        category_slug = self.kwargs.get('category_slug', None)
        pk = self.kwargs.get('pk', None)
        qs = Article.objects.filter(article_category__category_slug=category_slug,id=pk)
        return qs
    
    def dispatch(self, *args, **kwargs):
        try:
            return super().dispatch(*args, **kwargs)
        except Http404:
            return redirect('blog:filtered_category',category_slug=self.kwargs.get('category_slug'))
