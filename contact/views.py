from django.shortcuts import render

from django.views.generic import ListView 

from .models import Skill

# Create your views here.

class ContactView(ListView):
    template_name = "contact/contact.html"
    queryset = Skill.objects.all()
    context_object_name = "contacts"
