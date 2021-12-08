from django.urls import path, include
from . import  views

urlpatterns = [
    path("", views.site_index, name="site_index"),
    path("SolDevRes/", views.resume, name="resume"),
    path("projects/", views.project_index, name="project_index"),
    path("projects/<int:pk>", views.go_to_project, name="go_to_project"), #<int:pk> notation tells Django that the value passed in the URL is an integer, and its variable name is pk.
    path("git_notifications", views.git_notifications, name="git_notifications"), 
]