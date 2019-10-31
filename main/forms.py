from django import forms

from .models import Word




class InputForm(forms.Form):

    Enter_Word = forms.CharField(label='Enter Word', label_suffix=':', max_length=20)
    Meaning = forms.CharField(label='meaning', label_suffix='', widget=forms.Textarea)


class DictForm(forms.ModelForm):

    class Meta:
        model = Word
        fields = '__all__'
        widgets = {
            'first_definition': forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
            'second_definition': forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
            'third_definition': forms.Textarea(attrs={'cols': 50, 'rows': 4}), 
            'more_definitions': forms.Textarea(attrs={'cols': 50, 'rows': 4}),
        }
