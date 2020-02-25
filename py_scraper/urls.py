from django.urls import path, include
from . import  views

urlpatterns = [
    path("scrape_msnbc", views.scrape_msnbc, name="scrape_msnbc"),
    path("scrape_cnn", views.scrape_cnn, name="scrape_cnn"),
    path("scrape_fox", views.scrape_fox, name="scrape_fox"),
]