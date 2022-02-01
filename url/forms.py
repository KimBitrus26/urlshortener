from .models import ShortenURL
from django import forms

class CreateShortURLForm(forms.ModelForm):
    class Meta:
        model=ShortenURL
        fields = {'original_url'}

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }