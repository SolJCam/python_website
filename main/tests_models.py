from django.test import TestCase
from main.models import Project

# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        chat = Project.objects.create(title="Chat App", description="One to many online chat", technology="nodejs, socket.io and ExpressJS", github_url="https://github.com/SolJCam/socket.io")
        web_map = Project.objects.create(title="Folium Web Map", description="Beautiful animated web display of US gradient features", technology="python dateutil, MarkerCluster and Pandas", github_url="https://github.com/SolJCam/location_pyapp")
        site = Project.objects.create(title="Personal Webiste", description="My online project portfolio", technology="Django, Bootstrap4 and jQuery", github_url="https://github.com/SolJCam/python_website")

    def test_retrieve_by_some_attribute(self):
        app1 = Project.objects.get(id=1)
        app2 = Project.objects.get(title="Folium Web Map")
        app3 = Project.objects.get(description="My online project portfolio")


