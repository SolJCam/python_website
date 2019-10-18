from django import forms

from .models import Word




class InputForm(forms.Form):

    py_dictionary = forms.CharField(label='py_dictionary', label_suffix='', max_length=120)


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

    # name = forms.CharField(max_length=120, label_suffix='', widget=forms.HiddenInput())
    # first_definition = forms.CharField(max_length=250, label_suffix='', widget=forms.HiddenInput())
    # first_ex = forms.CharField(max_length=120, label_suffix='', widget=forms.HiddenInput())
    # second_definition = forms.CharField(max_length=250, label_suffix='', widget=forms.HiddenInput())
    # second_ex = forms.CharField(max_length=120, label_suffix='', widget=forms.HiddenInput())
    # third_definition = forms.CharField(max_length=250, label_suffix='', widget=forms.HiddenInput())
    # third_ex = forms.CharField(max_length=120, label_suffix='', widget=forms.HiddenInput())
    # synonym = forms.CharField(max_length=120, label_suffix='', widget=forms.HiddenInput())
    # more_definitions = forms.CharField(label_suffix='', widget=forms.HiddenInput())

    # class Meta:
    #     model = Word
    #     fields = ('name', 'first_definition', 'first_ex', 'second_definition', 'second_ex', 'third_definition', 'third_ex', 'synonym', 'more_definitions',)
    #     widgets = {
    #         'name': forms.HiddenInput(), 
    #         'first_definition': forms.HiddenInput(), 
    #         'first_ex': forms.HiddenInput(),
    #         'second_definition': forms.HiddenInput(), 
    #         'second_ex': forms.HiddenInput(), 
    #         'third_definition': forms.HiddenInput(), 
    #         'third_ex': forms.HiddenInput(), 
    #         'synonym': forms.HiddenInput(), 
    #         'more_definitions': forms.HiddenInput(),
    #     }


