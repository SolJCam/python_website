from django import forms

from .models import Word
from django.core.exceptions import ValidationError


def validate_num_length(num):
    if num > 9999:
        raise ValidationError(
            (f"{num} is too large. Enter a value that\'s equal to 4 digits or less"), code='too large'
        )



class InputForm(forms.Form):

    Enter_Word = forms.CharField(label='Enter Word', label_suffix=':', max_length=20)
    Meaning = forms.CharField(label='meaning', label_suffix='', widget=forms.Textarea)


class DictForm(forms.ModelForm):

    creator = forms.IntegerField(validators=[validate_num_length])

    class Meta:
        model = Word
        fields = '__all__'
        widgets = {
            'first_definition': forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
            'second_definition': forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
            'third_definition': forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
            'more_definitions': forms.Textarea(attrs={'cols': 50, 'rows': 4}),
        }
