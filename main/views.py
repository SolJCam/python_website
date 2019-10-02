from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main.models import Project, Word
from .forms import DictForm
#from django.urls import reverse_lazy
import pdb #python debugger

# Create your views here.
def site_index(request):
  projects = Project.objects.all()
  context = {
      'projects': projects
  }
  # pdb.set_trace()
  return render(request, 'index.html', context)

def project_index(request):
  projects = Project.objects.all()

  if request.method == 'POST':
    # create a form instance and populate it with data from the request:
    req = DictForm(request.POST)
    
    # check whether it's valid:
    if req.is_valid():
      # If True, will be able to find all the validated form data in its cleaned_data attribute and use it to update the database etc
      form = Word.objects.using('dictionary').get(name=req.cleaned_data['py_dictionary'])      
  # if a GET (or any other method) we'll create a blank form
  else:
    form = DictForm() 

  context = {
      'projects': projects,
      'form': form,
  }

  return render(request, 'local_apps.html', context)


model = Word
fields = [
  "name",
  "first_definition",
  "first_ex",
  "second_definition",
  "second_ex",
  "third_definition",
  "third_ex",
  "synonym",
]

def WordCreate(CreateView):
  model
  fields 

def WordUpdate(UpdateView):
  model
  fields

def WordDelete(DeleteView):
  model













# Below will be to visit indivudual project urls. Not ready
def project_detail(request, pk):
  projects = get_object_or_404(Project.objects.get(pk=pk))
  context = {
    'projects': projects
  }
  return render(request, 'pydictionary.html', context)
