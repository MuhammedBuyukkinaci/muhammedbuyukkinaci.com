from django.shortcuts import render

from django.views.generic import ListView 

from .models import Skill, Page

# Create your views here.

class ContactView(ListView):
    template_name = "contact/contact.html"
    queryset = Skill.objects.all()
    context_object_name = "contacts"

    def get_queryset(self):
        # original qs
        qs = super().get_queryset() 
        # filter by a variable captured from url, for example
        return qs.filter(skill_percent__gte=20).order_by('-skill_percent')

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['socialmedias'] = Page.objects.filter(page_category='socialmedia')
        data['businesses'] = Page.objects.filter(page_category='business')
        return data