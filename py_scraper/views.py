from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
import pdb 

def py_scraper(request):

  context = {

  }
  
  return render(request, 'py_scraper.html', context)