from django.shortcuts import render
from django.views.generic import ListView
from .models import Homepage
from random import randint

# Create your views here.

class HomeView(ListView):
    model = Homepage
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        count = Homepage.objects.count()
        data['homepage'] = Homepage.objects.all()[randint(0, count - 1)] 
        return data