from django.shortcuts import render

from django.views.generic import ListView

from .models import Testimonial

# Create your views here.
class TestimonialView(ListView):
    template_name = "testimonials/testimonials.html"
    queryset = Testimonial.objects.all()
    context_object_name = "testimonials"