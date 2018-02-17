import os

from django.conf import settings
from django.forms import model_to_dict
from django.shortcuts import get_object_or_404, render

from . import forms, models


def index(request):

    if request.method == 'GET':
        search_query = request.GET.get('search_box', None)

        if search_query is not None:
            person = get_object_or_404(models.Person, email=search_query)
            form = forms.NfeForm(model_to_dict(person))
        else:
            form = forms.NfeForm()

    elif request.method == 'POST':
        form = forms.NfeForm(request.POST)

        if form.is_valid():
            nfe_txt_creator(form)

    return render(request, 'index.html', {'form': form})


def nfe_txt_creator(form):
    email = str(form.cleaned_data.get('email'))
    file_path = os.path.join(settings.BASE_DIR, f'nfe-{email}.txt')
    with open(file_path, 'w') as file:
        write_file(file, form)


def write_file(file, form):
    nfe_txt = 'Nome: {}\nCPF: {}\nE-Mail: {}\nData de nascimento: {}'
    nfe_txt = nfe_txt.format(
        form_field(form, 'name'),
        form_field(form, 'cpf'),
        form_field(form, 'email'),
        form_field(form, 'birth_date')
    )
    file.write(nfe_txt)


def form_field(form, field):
    return str(form.cleaned_data.get(field))
