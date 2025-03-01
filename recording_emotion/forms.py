from django import forms
from .models import RecordingEmotion

class RecordingEmotionForm(forms.ModelForm):
    class Meta:
        model = RecordingEmotion
        fields = ['emotion', 'description_day', 'discovery']
        widgets = {
            'emotion': forms.Select(attrs={'class': 'form-select border-success border-2'}),
            'description_day': forms.Textarea(attrs={'class': 'form-control border-success border-2', 'rows': 5}),
            'discovery': forms.Textarea(attrs={'class': 'form-control border-success border-2', 'rows': 2}),
        }