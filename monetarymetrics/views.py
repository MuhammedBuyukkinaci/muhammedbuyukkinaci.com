from django.shortcuts import render
from django.views.generic import ListView,View

# Create your views here.

class MonetaryMetricsView(ListView):
    def get_queryset(self):
        return None
    template_name = "monetarymetrics/monetarymetrics.html"