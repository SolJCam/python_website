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
            'name': forms.HiddenInput(),
            'first_definition': forms.HiddenInput(), 
            'first_ex': forms.HiddenInput(),
            'second_definition': forms.HiddenInput(), 
            'second_ex': forms.HiddenInput(), 
            'third_definition': forms.HiddenInput(), 
            'third_ex': forms.HiddenInput(), 
            'synonym': forms.HiddenInput(), 
            'more_definitions': forms.HiddenInput(),
        }


