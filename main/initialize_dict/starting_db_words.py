from django.shortcuts import get_object_or_404, render
import json


def display_words():
    with open("./dictionary.json") as f:

      for word in f:
        display = "<p>{0}</p><br>".format(word)
      
      nu_file = open("./test.html", "w")
      nu_file.write(display)
    
    json_words = open("./dictionary.json")
    read_json = json_words.read()
    dict_words = json.loads(read_json)
    json_words.close()
    return print(dict_words)

display_words()