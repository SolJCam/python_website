from django.shortcuts import get_object_or_404, render
from main.models import Project #Word
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
  return render(request, 'pydictionary.html', context)

# Below will be to visit indivudual project urls. Needs refinement
def project_detail(request, pk):
  projects = get_object_or_404(Project.objects.get(pk=pk))
  context = {
    'projects': projects
  }
  return render(request, 'pydictionary.html', context)
