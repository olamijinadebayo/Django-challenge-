from django import forms
from django.core.validators import validate_email

from .models import Person

class PersonForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if Person.objects.filter(email=email).exists():
            raise forms.ValidationError('Email has been used already')
        return email
