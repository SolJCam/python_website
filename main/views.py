from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from main.models import Project, Word
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
  # words = Word.objects.all()
  context = {
      'projects': projects,
      # 'words': words
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
