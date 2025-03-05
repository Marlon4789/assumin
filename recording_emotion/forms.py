from django import forms
from .models import RecordingEmotion

class RecordingEmotionForm(forms.ModelForm):
    class Meta:
        model = RecordingEmotion
        fields = ['emotion', 'description_day']
        widgets = {
            'emotion': forms.Select(attrs={'class': 'form-select border-dark focus-ring focus-ring-secondary py-1 px-2 text-decoration-none'}),
            'description_day': forms.Textarea(attrs={'class': 'form-control border-dark focus-ring focus-ring-secondary py-1 px-2 text-decoration-none', 'rows': 10}),
            # 'discovery': forms.Textarea(attrs={'class': 'form-control border-dark border-1', 'rows': 2}),
        }