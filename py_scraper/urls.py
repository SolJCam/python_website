from django.urls import path, include
from . import  views

urlpatterns = [
    path("projects/<int:pk>", views.py_scraper, name="py_scraper")
]