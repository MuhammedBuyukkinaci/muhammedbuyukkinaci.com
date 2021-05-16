from django.urls import path
from .views import *

app_name = "photos"

urlpatterns = [
    path('',PhotosView.as_view(), name = 'photos'),
]
