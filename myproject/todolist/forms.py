from django import forms

class Check(forms.Form):
    condition = forms.BooleanField()