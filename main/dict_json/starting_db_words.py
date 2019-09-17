from django.shortcuts import get_object_or_404, render

with open("./dictionary.json") as f:
  
  for word in f:
    display = "<p>{0}</p><br>".format(word)
  render(display)