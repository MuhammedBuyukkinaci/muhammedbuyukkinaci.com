from django.shortcuts import render
from django.views.generic import ListView 
import random
from .models import Project,Detail
from random import shuffle

class ProjectView(ListView):
    template_name = "projects/projects.html"
    model = Project


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['projects'] = sorted(Project.objects.all(), key=lambda x: random.random())
        data['details'] = Detail.objects.all().order_by('detail_number')
        return data