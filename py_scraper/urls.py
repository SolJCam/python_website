from django.urls import path, include
from . import  views

urlpatterns = [
    path("", views.py_scraper, name="py_scraper"),
    path("scrape_msnbc", views.py_scraper, name="scrape_msnbc"),
    path("scrape_fox", views.py_scraper, name="scrape_fox"),
    path("scrape_cnn", views.py_scraper, name="scrape_cnn"),
]