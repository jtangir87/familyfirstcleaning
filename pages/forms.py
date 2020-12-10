from django import forms
from django.forms.fields import CharField


class RequestQuoteForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=12)
    email = forms.EmailField()
