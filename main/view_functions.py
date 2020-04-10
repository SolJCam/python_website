from .models import Word
from difflib import SequenceMatcher, get_close_matches
from django.core.exceptions import ObjectDoesNotExist
from random import randint
import pdb, json


json_words = open("main/dictionary.json")
read_json = json_words.read()
dict_words = json.loads(read_json)
json_words.close()
    

#function for checking user dictionary input and offering suggestions
def suggest_words(word):
    stringyfy_dict = list(map(lambda x: str(x).split(":")[0], dict_words))
    suggestions = get_close_matches(word, stringyfy_dict)
    # pdb.set_trace()
    reply = [f"{word} is not in the dictionary. Click on a spelling suggestion below or try again:", suggestions]
    return reply


#function for testing variations of word against json file then database and returning best result or suggestions if necessary
def get_meaning(wrd_input):
    word = wrd_input.lower()
    try:
      meaning = dict_words[word][0]
    except:
      word = wrd_input.title()
      try:
        meaning = dict_words[word][0]
      except:
        word = wrd_input.upper()
        try:
          meaning = dict_words[word][0]
        except: 
          word = wrd_input.lower()
          try:
            meaning = str(Word.objects.get(word=word))
          except:
            word = wrd_input.title()
            try:
              meaning = str(Word.objects.get(word=word))
            except:
              word = wrd_input.upper()
              try:
                meaning = str(Word.objects.get(word=word))
              except: 
                meaning = suggest_words(wrd_input)
    pdb.set_trace()
    return meaning


#function for creating and saving word to database
def add_word(usr_wrd):
    # pdb.set_trace
    nu_word = Word.objects.create(
        word = usr_wrd["word"],
        definition = usr_wrd["definition"],
        second_definition = usr_wrd["second_definition"],
        more_definitions = usr_wrd["more_definitions"],
        creator = randint(1, 9999)
    )

    nu_word.save()
    return f"You have successfully added {usr_wrd['word']} to the dictionary!"