from django import forms

class DictForm(forms.Form):
    py_dictionary = forms.CharField(label='py_dictionary', max_length=120)