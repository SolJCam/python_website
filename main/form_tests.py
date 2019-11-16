from django.test import TestCase
from main.models import Project, Word
from django.urls import reverse
import json
import pdb

# ex. to test only one method: ./manage.py test main.tests.ProjectTestCase.<method>  



class ProjectTestCase(TestCase):
    multi_db = True
    # Test ability to retrieve Projects from db
    def setUp(self):
        


