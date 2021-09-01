from django.shortcuts import render
from django.views.generic import ListView,View
from .models import Image

# Create your views here.

class PhotosView(ListView):
    # def get_queryset(self):
    #     return None
    model = Image
    template_name = "photos/photos.html"