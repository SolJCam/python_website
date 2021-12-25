from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Word



class InputForm(forms.Form):

    Enter_Word = forms.CharField(label='Enter Word', max_length=20)
    Error = forms.CharField(label='Error')
    Meaning = forms.CharField(label='meaning', widget=forms.Textarea)
    Success = forms.CharField(label='Success!')


def validate_word(word):
    pattern = r"[^A-Za-z]"
    if re.findall(pattern, word):
        raise ValidationError(
            ("%{value} has invalid characters. Only characters a-z, A-Z, '.' and '-' are acceptable. Please try again"), 
            code='invalid characters',
            params={'value': word}
        )


class DictForm(forms.ModelForm):

    word = forms.CharField(label='New Word', max_length=20, validators=[validate_word])
    definition = forms.CharField(label='Definition', max_length=500, widget = forms.Textarea(attrs={'placeholder':'Include examples using the word and synonyms','cols': 30, 'rows': 6}))
    second_definition = forms.CharField(label='Second Definition', required=False, max_length=500, widget = forms.Textarea(attrs={'placeholder':'Include examples using the word and synonyms','cols': 30, 'rows': 4}))
    more_definitions = forms.CharField(label='More Definitions', required=False, max_length=500, widget = forms.Textarea(attrs={'placeholder':'Include examples using the word and synonyms','cols': 30, 'rows': 4}))

    class Meta:
        model = Word
        fields = '__all__'