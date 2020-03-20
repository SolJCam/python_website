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
        py_dict = Project.objects.create(title="py_dictionary", description="online dictionary which allows users to save their own words to a postgresql db", technology="difflib.SequenceMatcher, difflib.get_close_matches, Django, Bootstrap, PostgreSQL")
        chat = Project.objects.create(title="Chat App", description="One to many online chat", technology="nodejs, socket.io and ExpressJS", github_url="https://github.com/SolJCam/socket.io")
        web_map = Project.objects.create(title="Folium Web Map", description="Beautiful animated web display of US gradient features", technology="python dateutil, MarkerCluster and Pandas", github_url="https://github.com/SolJCam/location_pyapp")
        py_scraper = Project.objects.create(title="py_scraper", description="Scrape the headlines of the homepages of the news networks CNN, FOX News and MSNBC and generate a wordcloud from the result", technology="BeautifulSoup, Word Cloud API")

    def retrieve_project_by_some_attribute(self):
        app1 = Project.objects.get(id=1)
        app2 = Project.objects.get(title="Folium Web Map")
        app3 = Project.objects.get(description="My online project portfolio")

    # Test View Context: currently failing
    def check_context_obj(self):
        # url = reverse('site_index')
        url = reverse('project_index')
        resp = self.client.get(url)

        # self.assertTrue(resp.context['projects'])
        # self.assertEqual(resp.context['projects'], Project.objects.all())
        self.assertTrue(resp.context['form'])
        # self.assertEqual(resp.context['projects'], Project.objects.all())

    # Test ability to create Word objects    
    def create_word_test(self):
        word = Word.objects.using('dictionary').create(word="ether", definition="A colorless liquid, slightly soluble in water; used as a reagent, intermediate, anesthetic, and solvent.\\n(Source: MGH)", second_definition="A class of chemical compounds which contain an oxygen atom connected to two (substituted) alkyl groups.", third_definition="", more_definitions="(substituted) alkyl groups.")
        get_word = Word.objects.using('dictionary').get(word="ether")

    # Test logic for parsing dictionary json file and saving to databse
    def make_dict(self):
        json_words = open("./initialize_dict/dictionary.json")
        read_json = json_words.read()
        dict_words = json.loads(read_json)
        small_d = dict(list(dict_words.items())[:5000])
        json_words.close()

        for word in small_d:
            pdb.set_trace()

            first = small_d[word][0]
            if len(small_d[word])>1 and len(small_d[word])<2:
                second = small_d[word][1]
                nu_word = Word.objects.using('dictionary').create(word=word, definition=first, second_definition=second, third_definition="", more_definitions="")
            elif len(small_d[word])>2 and len(small_d[word])<3:
                second = small_d[word][1]
                third = small_d[word][2]
                nu_word = Word.objects.using('dictionary').create(word=word, definition=first, second_definition=second, third_definition=third, more_definitions="")
            elif len(small_d[word])>3:
                # pdb.set_trace()
                second = small_d[word][1]
                third = small_d[word][2]
                additional = []
                diff = len(small_d[word])-3
                for x in range(diff):
                    additional.append(small_d[word][3+x])
                nu_word = Word.objects.using('dictionary').create(word=word, definition=first, second_definition=second, third_definition=third, more_definitions=additional)
            else:
                nu_word = Word.objects.using('dictionary').create(word=word, definition=first, second_definition="", third_definition="", more_definitions="")

            nu_word.save()

            # print(nu_word)

