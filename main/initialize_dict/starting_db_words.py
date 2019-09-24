# from django.shortcuts import get_object_or_404, render
from main.models import Word
import json
import pdb 

def display_words():
    # with open("./dictionary.json") as f:

      # for word in f:
      #   display = "<p>{0}</p><br>".format(word)
      
      # nu_file = open("./test.html", "w")
      # nu_file.write(display)
    
    json_words = open("./dictionary.json")
    read_json = json_words.read()
    dict_words = json.loads(read_json)
    json_words.close()
    # small_d = dict(list(dict_words.items())[:11])

    for word in dict_words:
      pdb.set_trace()
      if word != Word.objects.using('dictionary').get(name=word):
        if dict_words[word[1]]:
          second = dict_words[word[1]]
        elif dict_words[word[2]]:
          third = dict_words[word[2]]
        elif len(dict_words[word])>3:
          diff = len(dict_words[word])-3
          additional = [ dict_words[word[2+x]] for x in range(diff) ]
        
        nu_word = Word.objects.using('dictionary').create(name=word, first_definition=dict_words.word[0], second_definition=second, third_definition=third, more_definitions=additional)
        nu_word.save(using='dictionary')

    return print(nu_word)

display_words()



