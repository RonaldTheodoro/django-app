from django import forms


class NfeForm(forms.Form):
    name = forms.CharField()
    cpf = forms.CharField()
    email = forms.EmailField()
    birth_date = forms.DateField()
    products = forms.CharField(widget=forms.Textarea)
