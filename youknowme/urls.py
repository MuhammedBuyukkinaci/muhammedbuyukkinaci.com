from django.urls import path
from .views import *

app_name = "youknowme"

urlpatterns = [
    path('',YouKnowMeView.as_view(), name = 'youknowme'),
]
