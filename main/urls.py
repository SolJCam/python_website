from django.urls import path, include
from . import  views

urlpatterns = [
    path("", views.site_index, name="site_index"),
    path("projects/", views.project_index, name="project_index"),
    path("projects/<int:pk>", views.ext_project, name="external_project") #<int:pk> notation tells Django that the value passed in the URL is an integer, and its variable name is pk.
]