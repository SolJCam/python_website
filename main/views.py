from django.shortcuts import render
from .models import Project, Word
from .forms import InputForm, DictForm
from django.core.exceptions import ObjectDoesNotExist
from difflib import SequenceMatcher, get_close_matches
import pdb #python debugger




#function for checking user dictionary input and offering suggestions
def suggest_words(word):
    dictionary = Word.objects.using('dictionary').all()
    stringyfy_dict = list(map(lambda x: str(x).split(":")[0], dictionary))
    suggestions = get_close_matches(word, stringyfy_dict)
    # pdb.set_trace()
    reply = [f"{word} is not in the dictionary. Click on a spelling suggestion below or try again:",]
    if len(suggestions) > 0:
        reply.append(suggestions)
    return reply




def site_index(request):
  projects = Project.objects.all()
  context = {
      'projects': projects
  }
  # pdb.set_trace()
  return render(request, 'index.html', context)



def project_index(request):

  #Create empty form for dictionary word search
  form = InputForm()
  add_word_form  = DictForm()
  projects = Project.objects.all()

  # pdb.set_trace()
  if request.POST:
    # create a form instance and populate it with data from the request:
    new_word = DictForm(request.POST)
    # check whether it's valid:
    pdb.set_trace()
    # if new_word.is_valid():
        # try:
        #   Word.objects.using('dictionary').get(name=new_word.cleaned_data['py_dictionary'])
        # except:

    #   Word.objects.using('dictionary').create(word=, first_definition=, second_definition=, third_definition=, more_definitions=)
        
  #if GET attribute has dict containing data, then this was a user search request. Proceed to processing and returing results  
  if bool(request.GET) == True:

    word = request.GET["Enter_Word"].lower()
    try:
      meaning = str(Word.objects.using('dictionary').get(word=word))
    except ObjectDoesNotExist:
      word = request.GET["Enter_Word"].title()
      try:
        meaning = str(Word.objects.using('dictionary').get(word=word))
      except ObjectDoesNotExist:
        word = request.GET["Enter_Word"].upper()
        try:
          meaning = str(Word.objects.using('dictionary').get(word=word))
        except ObjectDoesNotExist: 
          word = request.GET["Enter_Word"]
          # meaning = suggest_words(word)
          suggestions = {}
          suggested = suggest_words(word)
          for ec in suggested[1]:
            suggestions[ec] = f'{ec}_id'
          meaning = [suggest_words(word)[0], suggestions]
  
    form = InputForm({'Meaning': meaning })
    # pdb.set_trace()
     
  context = {
      'form': form,
      'add_word': add_word_form,
      'projects': projects,
  }

  return render(request, 'local_apps.html', context)



# Below will be to visit indivudual project urls. Not ready
def project_detail(request, pk):
  projects = get_object_or_404(Project.objects.get(pk=pk))
  context = {
    'projects': projects
  }
  return render(request, 'pydictionary.html', context)




















  # if request.method == 'POST':
  #   # create a form instance and populate it with data from the request:
  #   form = NameForm(request.POST)
  #   # check whether it's valid:
  #   if form.is_valid():
  #       # process the data in form.cleaned_data as required
  #       # ...
  #       # redirect to a new URL:
  #       return HttpResponseRedirect('/thanks/')
        
  # #if GET attribute returns empty dict, proceed with generating blank model form
  # else:


      # try:
    #   form = Word.objects.using('dictionary').get(name=user_input)
    # except:


    #bound dict from GET request containing user input to a form instance
    # req = DictForm(request.GET)
    # # pdb.set_trace()

    # # check whether bound dict is valid (Django does some magic in the background to accomplish this):
    # if req.clean(['name', 'first_definition']):
    # # if req.is_valid(): #for reqular form validation
    #   pdb.set_trace()

    #   # If True, will be able to find all the validated form data in its cleaned_data attribute and use it to update the database etc
    #   form = Word.objects.using('dictionary').get(name=req.cleaned_data['py_dictionary'])