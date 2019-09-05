from django.urls import path, include
from . import  views

urlpatterns = [
    path("", views.site_index, name="site_index"),
    path("projects", views.project_index, name="project_index"),
    # path('portfolio/', include("folium_web_map.urls")),
    # path("projects/<int:pk>", views.project_detail, name="project_detail") #<int:pk> notation tells Django that the value passed in the URL is an integer, and its variable name is pk.
]