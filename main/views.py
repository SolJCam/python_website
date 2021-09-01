from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse
import requests, yagmail, json, pdb #python debugger
from .models import Project, Word
from .forms import InputForm, DictForm
from .view_functions import get_meaning, add_word



def site_index(request):
  projects = Project.objects.all()
  new_email = ""
  # encrypt_oauth()

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

    yag = yagmail.SMTP(server_email, oauth2_file="main/oauth2_creds.json")  # oauth parameter actually generates this file; no need to create
    # pdb.set_trace()
    yag.send(
      to=server_email,
      subject=Subject,
      contents=body, 
    )
    print(new_email)

  context = {
      'projects': projects,
  }
  return render(request, 'index.html', context)



def git_notifications(request):

  headers = { 'Accept': 'application/vnd.github.v3+json'}

  req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers, auth=("username","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"))
  # req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers)
  # print(req.json())

  list_of_portfolio_projects = [
      'python_website',
      'React-Search-Pics',
      'React-Search-Videos',
      'react-songs',
      'react-twitch-clone',
      'React-Widgets',
      'socket.io'
  ]

  list_of_repos = req.json()

  project = ''
  message = ''
  date = ''

  dictionary_of_repos = {}
  
  for repo in list_of_repos:
      if repo['name'] in list_of_portfolio_projects:
          commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits" )
          # print(commits_by_project.json()[0]['commit']['message'])
          # print(repo['name'])
          # print(f"https://api.github.com/repos/SolJCam/#{repo['name']}/commits")

          project = repo['name']
          message = commits_by_project.json()[0]['commit']['message']
          date = commits_by_project.json()[0]['commit']['author']['date']

          dictionary_of_repos[repo['name']] = [project,message,date]
          
          print(dictionary_of_repos)
          # print(project+'\n'+message+'\n'+date+'\n')

  try:
    # pdb.set_trace()
    response = JsonResponse(dictionary_of_repos)
    return response
    # return JsonResponse([project, message, date], safe=False)
  except:
    return HttpResponseNotFound(status=500)



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

      # pdb.set_trace()
    else:
      # pdb.set_trace()
      error = new_word.errors.as_data()

      try:
        if error['word']:
          form = InputForm({'Error':" The word entered has invalid characters. Only characters a-z, A-Z, '.' and '-' are acceptable. Please try again" })
      except:
        form = InputForm({'Error':" There was an unknown server error.\n Please enter the word again" })
      
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
  elif 'py_dictionary' == proj:
    return project_index(request)
  else:
    project = Project.objects.get(id=pk)
    html = project.title+'.html'
    context = {
      'project': project
    }
    return render(request, html, context)