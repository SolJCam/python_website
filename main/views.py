from django.shortcuts import render, redirect
from django.http import JsonResponse
import yagmail, json, pdb #python debugger
from .models import Project, Word
from .forms import InputForm, DictForm
from .view_functions import get_meaning, add_word




def site_index(request):
  projects = Project.objects.all()
  new_email = ""

  if request.method == "POST":
    # pdb.set_trace()

    server_email = "soljerrold13@gmail.com"
    new_email = json.loads(request.body)
    Subject = new_email['Subject']
    body = '''
      {Name}
      {Email}
      
      {Msg}
    '''.format(Name = new_email['Body'][1], Email = new_email['Body'][0], Msg = new_email['Body'][2])

    # pdb.set_trace()
    yag = yagmail.SMTP(server_email, oauth2_file="main/oauth2_creds.json")
    yag.send(
      to=server_email,
      subject=Subject,
      contents=body, 
    )
    print(new_email)
    return JsonResponse({'ok':True}, status=200)

  context = {
      'projects': projects,
  }
  return render(request, 'index.html', context)




def resume(request):
  context = {
    'context': "some context...",
  }
  return render(request, 'pdf.html', context)





def project_index(request):

  #Create empty form for dictionary word search
  form = InputForm()
  add_word_form  = DictForm()
  projects = Project.objects.all()

  # pdb.set_trace()
  # if request.method == "POST":
  if bool(request.POST) == True:
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
      
  # request.GET returns QueryDict which, if empty, is therefore "false" and code moves on to render projects page. 
  # If QueryDict contains data then this was a dictonary search request. Proceed to processing and returing results  
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
  proj = Project.objects.get(id=pk).title
  if 'js_ChatApp' == proj:
    response = redirect('https://solschatroom.herokuapp.com/')
    return response
  else:
    project = Project.objects.get(id=pk)
    html = project.title+'.html'
    context = {
      'project': project
    }
    return render(request, html, context)