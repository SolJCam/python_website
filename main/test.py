from django.test import TestCase
from main.models import Project, Word
from django.urls import reverse

# to test only one method: ./manage.py test main.tests.ProjectTestCase.<method>  



class ProjectTestCase(TestCase):
    # Test ability to retrieve Projects from db
    def setUp(self):
        chat = Project.objects.create(title="Chat App", description="One to many online chat", technology="nodejs, socket.io and ExpressJS", github_url="https://github.com/SolJCam/socket.io")
        web_map = Project.objects.create(title="Folium Web Map", description="Beautiful animated web display of US gradient features", technology="python dateutil, MarkerCluster and Pandas", github_url="https://github.com/SolJCam/location_pyapp")
        site = Project.objects.create(title="Personal Webiste", description="My online project portfolio", technology="Django, Bootstrap4 and jQuery", github_url="https://github.com/SolJCam/python_website")

    def retrieve_project_by_some_attribute(self):
        app1 = Project.objects.get(id=1)
        app2 = Project.objects.get(title="Folium Web Map")
        app3 = Project.objects.get(description="My online project portfolio")

    # Test View Context: currently failing
    def check_context_obj(self):
        url = reverse('site_index')
        resp = self.client.get(url)

        self.assertTrue(resp.context['projects'])
        self.assertEqual(resp.context['projects'], Project.objects.all())

    # Test ability to create Word objects    
    def create_word_test(self):
        word = Word.objects.create(name="ether", first_definition="A colorless liquid, slightly soluble in water; used as a reagent, intermediate, anesthetic, and solvent.\\n(Source: MGH)", second_definition="A class of chemical compounds which contain an oxygen atom connected to two (substituted) alkyl groups.", third_definition="", more_definitions="(substituted) alkyl groups.")

