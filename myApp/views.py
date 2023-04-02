"""
from django.shortcuts import render, redirect
from myApp.models import Element
from django.contrib import messages

from django.http import JsonResponse
from myApp.models import Element, Person

def entry(request, id):
    element = Element.objects.get(id=id)
    data = {
        'id': element.id,
        'username': element.username,
        'value': element.value
    }
    return JsonResponse(data)


from .forms import QuoteForm

def add_joke(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QuoteForm()

    # Ajouter cette ligne pour récupérer les personnes de la base de données
    persons = Person.objects.all()

    context = {
        'form': form,
        'persons': persons, # Ajouter cette variable au contexte
    }
    return render(request, 'myApp/add_joke.html', context)

from .models import Person, Quote
from .forms import QuoteForm

def add_joke(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            person_id = request.POST.get('person')
            person = Person.objects.get(pk=person_id)
            quote = form.save(commit=False)
            quote.person = person
            quote.save()
            return redirect('myApp:index')
    else:
        form = QuoteForm()
    return render(request, 'myApp/add_joke.html', {'form': form, 'persons': Person.objects.all()})



def index(request):
    elements = Element.objects.all()
    context = {'elements': elements}

    last_element_added_id = request.session.get('last_element_added', None)

    for element in elements:
        if element.id == last_element_added_id:
            element.is_last_added = True
        else:
            element.is_last_added = False

    return render(request, 'myapp/index.html', context)


def get_authors(request):
    persons = Person.objects.all()
    return render(request, 'app/authors.html', {'persons': persons})


def delete_all(request):
    Element.objects.all().delete()
    return redirect('myApp:index')
"""

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Element, Person, Quote
from .forms import QuoteForm

def index(request):
    quotes = Quote.objects.all()
    context = {'quotes': quotes}
    return render(request, 'myApp/index.html', context)

from django.shortcuts import render
from django.http import HttpResponse

def add_element(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            person_id = request.POST.get('person')
            person = Person.objects.get(pk=person_id)
            quote = form.save(commit=False)
            quote.person = person
            quote.save()
            return redirect('myApp:index')
    else:
        form = QuoteForm()
    return render(request, 'myApp/add_joke.html', {'form': form, 'persons': Person.objects.all()})


def get_authors(request):
    authors = Person.objects.all()
    return render(request, 'myApp/authors.html', {'authors': authors})


def get_elements(request):
    elements = Quote.objects.all().order_by('id')
    elements_list = [{'element': elem.value, 'person': elem.person.name} for elem in elements]
    if len(elements_list) > 0:
        elements_list[-1]['is_last_added'] = True
    return render(request, 'myApp/index.html', {'elements': elements_list})


def delete_all(request):
    Element.objects.all().delete()
    return HttpResponseRedirect(reverse('myApp:index'))
