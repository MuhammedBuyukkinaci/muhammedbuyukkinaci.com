from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import Category, Article

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
        qs = super().get_queryset()
        category_slug = self.kwargs.get('category_slug', None)
        qs = Article.objects.filter(article_category__category_slug=category_slug)
        return qs
    
    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['details'] = Detail.objects.all().order_by('detail_number')
    #     return data

class ArticleView(DetailView):
    template_name = "blog/article_detail.html"
    model = Article
    #context_object_name = "article"
    # Initial queryset of leads for the entire organisation