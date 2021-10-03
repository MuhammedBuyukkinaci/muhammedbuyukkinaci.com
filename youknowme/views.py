from django.shortcuts import render

from django.views.generic import ListView 

from contact.models import Skill, Page

class YouKnowMeView(ListView):
    model = Skill
    template_name = "youknowme/youknowme.html"


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['choices'] = range(4)
        return data