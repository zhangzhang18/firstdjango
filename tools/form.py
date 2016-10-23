from django import forms
from django.forms import ModelForm


class ADDForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
