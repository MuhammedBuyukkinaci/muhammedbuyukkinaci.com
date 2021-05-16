from django.shortcuts import render

from django.views.generic import ListView 

from .models import Project,Detail

class ProjectView(ListView):
    template_name = "projects/projects.html"
    queryset = Project.objects.all().order_by('?')
    context_object_name = "projects"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['details'] = Detail.objects.all().order_by('detail_number')
        return data