from django.shortcuts import render, get_object_or_404
from django.forms import model_to_dict

from . import models, forms

def index(request):

    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)

        if search_query is not None:
            person = get_object_or_404(models.Person, email=search_query)
            form = forms.NfeForm(model_to_dict(person))
        else:
            form = forms.NfeForm()

    elif request.method == 'POST':
        form = forms.NfeForm(request.POST)

        if form.is_valid():
            print('ok')

    return render(request, 'index.html', {'form': form})