from django import forms
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForms(UserCreationForm):
    email = forms.EmailField()
    nama = forms.CharField(max_length=60)

    class Meta:
        model = User
        fields = ["nama","username","email","password1","password2"]