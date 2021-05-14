from django.urls import path
from .views import *

app_name = "testimonials"

urlpatterns = [
    path('',TestimonialView.as_view(), name = 'testimonials'),
]