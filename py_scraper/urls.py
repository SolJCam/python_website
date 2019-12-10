from django.urls import path, include
from . import  views

urlpatterns = [
    path("", views.py_scraper, name="py_scraper")
]