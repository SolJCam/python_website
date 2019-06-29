from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index():
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)