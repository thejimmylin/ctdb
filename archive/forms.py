from django import forms

from .models import Archive


class ArchiveModelForm(forms.ModelForm):
    class Meta():
        model = Archive
        exclude = ['created_by']
