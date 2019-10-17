from django.shortcuts import render
from .models import Project, Word
from .forms import DictForm
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

  form = DictForm()

  #if GET attribute returns empty dict, proceed with generating blank model form
  if request.GET:
    user_input = request.GET["py_dictionary"]
    form = Word.objects.using('dictionary').get(name=user_input)

    #bound dict from GET request containing user input to a form instance
    # req = DictForm(request.GET)
    # # pdb.set_trace()

    # # check whether bound dict is valid (Django does some magic in the background to accomplish this):
    # if req.clean(['name', 'first_definition']):
    # # if req.is_valid(): #for reqular form validation
    #   pdb.set_trace()

    #   # If True, will be able to find all the validated form data in its cleaned_data attribute and use it to update the database etc
    #   form = Word.objects.using('dictionary').get(name=req.cleaned_data['py_dictionary'])
     
  context = {
      'projects': projects,
      'form': form,
  }

  return render(request, 'local_apps.html', context)



# Below will be to visit indivudual project urls. Not ready
def project_detail(request, pk):
  projects = get_object_or_404(Project.objects.get(pk=pk))
  context = {
    'projects': projects
  }
  return render(request, 'pydictionary.html', context)
