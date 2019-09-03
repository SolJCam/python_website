from django.shortcuts import render
from projects.models import Project

# Create your views here.
def site_index(request):
    return render(request, 'index.html')

def project_index(request):
    projects = Project.objects.all()
    context = {
        'project': projects
    }
    return render(request, 'pydictionary.html', context)

# Below will be to visit indivudual project urls
def project_detail(request, pk):
    projects = Project.objects.get(pk=pk)
    context = {
        'project': projects
    }
    return render(request, 'pydictionary.html', context)
