from django.shortcuts import render, redirect
from .models import Project, Word
from .forms import InputForm, DictForm
import pdb #python debugger
from .view_functions import get_meaning, add_word





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
        
      meaning = get_meaning(new_word.cleaned_data['word'])
      
      if len(meaning[1][0]) > 1:
        form = InputForm({"Success": add_word(new_word.cleaned_data)})
      else:
        form = InputForm({'Meaning': [f"{new_word.cleaned_data['word']} is already in the dictionary."]})

    else:
      # pdb.set_trace()
      error = new_word.errors.as_data()

      try:
        if error['word']:
          form = InputForm({'Error': " The word entered has invalid characters. Only characters a-z, A-Z, '.' and '-' are acceptable. Please try again" })
      except:
        form = InputForm({'Error': " There was an unknown server error.\n Please enter the word again" })
      
  #if GET attribute has dict containing data, then this was a user search request. Proceed to processing and returing results  
  if bool(request.GET) == True:

    word = request.GET["Enter_Word"]
    meaning = get_meaning(word)
  
    form = InputForm({'Meaning': meaning })
    # pdb.set_trace()
     
  context = {
      'form': form,
      'add_word': add_word_form,
      'projects': projects,
  }

  return render(request, 'local_apps.html', context)





def external_project(request, pk):
  # pdb.set_trace()
  if pk==2:
    response = redirect('https://solschatroom.herokuapp.com/')
    return response
  else:
    project = Project.objects.get(id=pk)
    context = {
      'project': project
    }
    return render(request, 'py_scraper.html', context)

