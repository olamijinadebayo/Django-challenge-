from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Person
from . forms import PersonForm
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render (request,'index.html')

def list(request):
    persons = Person.objects.all()
    return render(request,'list.html',{'persons':'persons'})

def add (request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            person = Person(name=name, email=email)
            person.save()
            return redirect('list')
    else:
        form = PersonForm()
    return render(request, 'add.html', {'form': form})
