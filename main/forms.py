from django import forms

# from .models import Word


class DictForm(forms.ModelForm):
    py_dictionary = forms.CharField(label='py_dictionary', max_length=120)

    class Meta:
        model = Word
        fields = ('name', 'first_definition', 'first_ex', 'second_definition', 'second_ex', 'third_definition', 'third_ex', 'synonym', 'more_definitions',)
        widgets = {
            'name': forms.HiddenInput(), 
            'first_definition': forms.HiddenInput(), 
            'first_ex', 'second_definition': forms.HiddenInput(), 
            'second_ex': forms.HiddenInput(), 
            'third_definition': forms.HiddenInput(), 
            'third_ex': forms.HiddenInput(), 
            'synonym': forms.HiddenInput(), 
            'more_definitions': forms.HiddenInput(),
        }


# class DictForm(forms.Form):
#     py_dictionary = forms.CharField(label='py_dictionary', max_length=120)