from django.shortcuts import render
from django.views.generic import ListView,View
from contact.models import Skill

# Create your views here.

class PhotosView(ListView):
    model = Skill
    template_name = "photos/photos.html"