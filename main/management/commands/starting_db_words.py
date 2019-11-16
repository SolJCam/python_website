# from django.shortcuts import get_object_or_404, render
# import pdb 
from django.core.management.base import BaseCommand
from main.models import Word
import json

class Command(BaseCommand):
    def handle(self):
    # with open("./dictionary.json") as f:

        # for word in f:
        #   display = "<p>{0}</p><br>".format(word)
        
        # nu_file = open("./test.html", "w")
        # nu_file.write(display)

        json_words = open("./dictionary.json")
        read_json = json_words.read()
        dict_words = json.loads(read_json)
        json_words.close()
        # print(len())
        # small_dict = dict(list(dict_words.items())[:1000])

        for word in dict_words:
            # pdb.set_trace()

            first = dict_words[word][0]
            if len(dict_words[word])>1 and len(dict_words[word])<2:
                second = dict_words[word][1]
                nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition=second, third_definition="", more_definitions="")
            elif len(dict_words[word])>2 and len(dict_words[word])<3:
                second = dict_words[word][1]
                third = dict_words[word][2]
                nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition=second, third_definition=third, more_definitions="")
            elif len(dict_words[word])>3:
                # pdb.set_trace()
                second = dict_words[word][1]
                third = dict_words[word][2]
                additional = []
                diff = len(dict_words[word])-3
                for x in range(diff):
                    additional.append(dict_words[word][3+x])
                nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition=second, third_definition=third, more_definitions=additional)
            else:
                nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition="", third_definition="", more_definitions="")

            nu_word.save()

            return print(nu_word)




