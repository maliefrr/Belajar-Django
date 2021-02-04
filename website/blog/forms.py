from django import forms
from .models import Comment
from django.core import validators

class CommentForm(forms.ModelForm):
    komentar = forms.CharField(required=True,
                            widget=forms.Textarea,
                            validators=[validators.MinLengthValidator(5)])
    class Meta:
        model = Comment
        fields = ['komentar']