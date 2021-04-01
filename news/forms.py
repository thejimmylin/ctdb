from django import forms

from .models import News


class NewsModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'at': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M',),
        }
        model = News
        exclude = ['created_by']
