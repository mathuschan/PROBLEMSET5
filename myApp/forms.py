from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('text', 'person')
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
            'person': forms.Select(attrs={'class': 'form-control'}),
        }
