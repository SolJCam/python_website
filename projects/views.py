from django.shortcuts import render
from projects.models import Project

# Create your views here.
def site_index(request):
    return render(request, 'index.html')

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects.html', context)

# To visit indivudual project urls
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
