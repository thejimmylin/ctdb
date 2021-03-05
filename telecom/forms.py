from django import forms

from .models import ContactTask


class ContactTaskModelForm(forms.ModelForm):

    class Meta():
        model = ContactTask
        exclude = []
