from django.urls import path
from .views import *

app_name = "monetarymetrics"

urlpatterns = [
    path('',MonetaryMetricsView.as_view(), name = 'monetarymetrics'),
]
