from django import forms
from django.core.exceptions import ValidationError

import re

from .models import Word




def validate_num_length(num):
    if num > 9999:
        raise ValidationError(
            (f"{num} is too large. Enter a value that\'s equal to 4 digits or less"), code='too large'
        )

def validate_word(word):
    pattern = r"[^A-Za-z]"
    if re.findall(pattern, word):
        raise ValidationError(
            (f"{word} has invalid characters. Only characters a-z, A-Z, '.' and '-' are acceptable. Please try again"), code='invalid characters'
        )



class InputForm(forms.Form):

    Enter_Word = forms.CharField(label='Enter Word', max_length=20)
    Error = forms.CharField(label='Error')
    Meaning = forms.CharField(label='meaning', widget=forms.Textarea)
    Success = forms.CharField(label='Success!')


class DictForm(forms.ModelForm):

    word = forms.CharField(label='New Word', label_suffix=':', max_length=20, validators=[validate_word])
    # creator = forms.IntegerField(label='Creator: a number < 9999', validators=[validate_num_length])

    class Meta:
        model = Word
        fields = '__all__'
        widgets = {
            'definition': forms.Textarea(attrs={'cols': 30, 'rows': 4}), 
            'example': forms.Textarea(attrs={'cols': 30, 'rows': 4}), 
            'synonym': forms.Textarea(attrs={'cols': 30, 'rows': 4}), 
        }
