from django import forms

# from .models import Word


class DictForm(forms.Form):
    py_dictionary = forms.CharField(label='py_dictionary', max_length=120)


# class DictForm(forms.Form):
#     py_dictionary = forms.CharField(label='py_dictionary', max_length=120)

#     class Meta:
#         # model = Word
#         fields = ('name', 'first_definition', 'first_ex', 'second_definition', 'second_ex', 'third_definition', 'third_ex', 'synonym', 'more_definitions',)
