from .models import Word
from difflib import SequenceMatcher, get_close_matches
from django.core.exceptions import ObjectDoesNotExist
import pdb


#function for checking user dictionary input and offering suggestions
def suggest_words(word):
    dictionary = Word.objects.using('dictionary').all()
    stringyfy_dict = list(map(lambda x: str(x).split(":")[0], dictionary))
    suggestions = get_close_matches(word, stringyfy_dict)
    # pdb.set_trace()
    reply = [f"{word} is not in the dictionary. Click on a spelling suggestion below or try again:", suggestions]
    return reply


#function for testing variations of word against database and returning best result
def check_dict(wrd_input):
    # pdb.set_trace()
    word = wrd_input.lower()
    try:
      meaning = str(Word.objects.get(name=word))
      # meaning = str(Word.objects.using('dictionary').get(word=word))
    except ObjectDoesNotExist:
      word = wrd_input.title()
      try:
        meaning = str(Word.objects.get(name=word))
        # meaning = str(Word.objects.using('dictionary').get(word=word))
      except ObjectDoesNotExist:
        word = wrd_input.upper()
        try:
          meaning = str(Word.objects.get(name=word))
          # meaning = str(Word.objects.using('dictionary').get(word=word))
        except ObjectDoesNotExist: 
          meaning = suggest_words(wrd_input)
    return meaning

def add_word(usr_wrd):
    # pdb.set_trace
    nu_word = Word.objects.create(
        name = usr_wrd["word"],
    # nu_word = Word.objects.using('dictionary').create(
    #     word = usr_wrd["word"],
        first_definition = usr_wrd["first_definition"],
        first_ex = usr_wrd["first_ex"],
        second_definition = usr_wrd["second_definition"],
        second_ex = usr_wrd["second_ex"],
        third_definition = usr_wrd["third_definition"],
        third_ex = usr_wrd["third_ex"],
        synonym = usr_wrd["synonym"],
        more_definitions = usr_wrd["more_definitions"],
        creator = usr_wrd["creator"]
    )

    nu_word.save()
    return f"You have successfully added {usr_wrd['word']} to the dictionary!"