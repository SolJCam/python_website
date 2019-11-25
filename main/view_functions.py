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
      meaning = str(Word.objects.using('dictionary').get(word=word))
    except ObjectDoesNotExist:
      word = wrd_input.title()
      try:
        meaning = str(Word.objects.using('dictionary').get(word=word))
      except ObjectDoesNotExist:
        word = wrd_input.upper()
        try:
          meaning = str(Word.objects.using('dictionary').get(word=word))
        except ObjectDoesNotExist: 
          meaning = suggest_words(wrd_input)
    return meaning

def add_word(usr_wrd):
    nu_word = Word.objects.using('dictionary').create(
        word = usr_wrd["word"],
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
    return nu_word


    # for word in small_d:
    #     pdb.set_trace()

    #     first = small_d[word][0]
    #     if len(small_d[word])>1 and len(small_d[word])<2:
    #         second = small_d[word][1]
    #         nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition=second, third_definition="", more_definitions="")
    #     elif len(small_d[word])>2 and len(small_d[word])<3:
    #         second = small_d[word][1]
    #         third = small_d[word][2]
    #         nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition=second, third_definition=third, more_definitions="")
    #     elif len(small_d[word])>3:
    #         # pdb.set_trace()
    #         second = small_d[word][1]
    #         third = small_d[word][2]
    #         additional = []
    #         diff = len(small_d[word])-3
    #         for x in range(diff):
    #             additional.append(small_d[word][3+x])
    #         nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition=second, third_definition=third, more_definitions=additional)
    #     else:
    #         nu_word = Word.objects.using('dictionary').create(word=word, first_definition=first, second_definition="", third_definition="", more_definitions="")

