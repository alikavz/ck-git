from django import forms
from .models import New


class NewAgePost(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title', 'text', 'authors', 'status']

