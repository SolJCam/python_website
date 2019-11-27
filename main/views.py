from django.shortcuts import render, get_object_or_404
from .models import Project, Word
from .forms import InputForm, DictForm
import pdb #python debugger
from .view_functions import suggest_words, check_dict, add_word





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
  if request.method == "POST":
    # create a form instance and populate it with data from the request:
    new_word = DictForm(request.POST)

    if new_word.is_valid():
        
        meaning = check_dict(new_word.cleaned_data['word'])
        
        if len(meaning[1][0]) > 1:
          form = InputForm({"Success": add_word(new_word.cleaned_data)})
        else:
          form = InputForm({'Meaning': [f"{new_word.cleaned_data['word']} is already in the dictionary."]})
        # pdb.set_trace()

    else:
      # pdb.set_trace()
      error = new_word.errors.as_data()

      try:
        if error['word']:
          form = InputForm({'Error': " The word entered has invalid characters. Only characters a-z, A-Z, '.' and '-' are acceptable. Please try again" })
      except:
        try:
          if error['creator']:
            form = InputForm({'Error': " The value entered for creator is too large.\n Please try again with a value 4 charaters or less" })
        except:
          form = InputForm({'Error': " There was an unknown server error.\n Please enter the word again" })
      
  #if GET attribute has dict containing data, then this was a user search request. Proceed to processing and returing results  
  if bool(request.GET) == True:

    word = request.GET["Enter_Word"]
    meaning = check_dict(word)
  
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


            # try:
        #   Word.objects.using('dictionary').get(name=new_word.cleaned_data['py_dictionary'])
        # except:
    #   Word.objects.using('dictionary').create(word=, first_definition=, second_definition=, third_definition=, more_definitions=)  