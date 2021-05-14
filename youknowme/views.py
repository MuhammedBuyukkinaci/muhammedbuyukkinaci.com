from django.shortcuts import render

from django.views.generic import ListView 

from contact.models import Skill, Page

class YouKnowMeView(ListView):
    model = Skill
    template_name = "youknowme/youknowme.html"
