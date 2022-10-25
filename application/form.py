from django import forms


class Userform(forms.Form):
    fio = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control shadow',
               'id': 'validationCustom01', 'name': 'fio', 'style': 'width: 70%'}
    ))
