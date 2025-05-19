from django import forms
from .models import AddNewIdeas

class AddNewIdeasForm(forms.ModelForm):
    class Meta:
        model = AddNewIdeas
        fields = ['idea']
        widgets = {
            'idea':  forms.Textarea(attrs={'class': 'form-control focus-ring focus-ring-secondary py-1 px-2 text-decoration-none', 'rows': 13, 'placeholder': '¿Cual es tu idea?'}),
        }
        labels = {
            'idea': '¿Cuál es tu idea?',
        }