from django.shortcuts import render

from django.views.generic import ListView

from .models import Category, Article

# Create your views here.

class BlogCategoriesView(ListView):
    template_name = "blog/blog_categories.html"
    queryset = Category.objects.all()
    context_object_name = "categories"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs

class ArticleView(ListView):
    pass
    # template_name = "projects/projects.html"
    # queryset = Project.objects.all().order_by('?')
    # context_object_name = "projects"

    # def get_context_data(self, **kwargs):
    #     data = super().get_context_data(**kwargs)
    #     data['details'] = Detail.objects.all().order_by('detail_number')
    #     return data