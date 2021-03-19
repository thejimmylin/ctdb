from django import forms
from .models import News


class NewsModelForm(forms.ModelForm):
    class Meta():
        model = News
        exclude = []
