from django import forms
from . import models
import numpy as np

YEARS = list(range(1900, 2025))

class FormLogin(forms.Form):
    login = forms.CharField(required=False, label="Login")
    password = forms.CharField(required=False, widget=forms.PasswordInput, label='Password')

class FormPatient(forms.ModelForm):

    """
    Firstname = forms.CharField(required=True)
    Lastname = forms.CharField(required=True)
    Birthdate = forms.DateField(required=True, widget=forms.SelectDateWidget(years=YEARS))
    Login = forms.CharField(required=True)
    Password = forms.CharField(required=True, widget=forms.PasswordInput)
    """
    class Meta:
        model = models.Patient
        fields = "__all__"
        widgets = {'birthdate' : forms.SelectDateWidget(years=YEARS),
                   'password' : forms.PasswordInput
                   }