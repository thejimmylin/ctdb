from django import forms

from .models import Email, ContactTask


class EmailModelForm(forms.ModelForm):
    class Meta():
        model = Email
        exclude = ['created_by', ]


class ContactTaskModelForm(forms.ModelForm):
    class Meta():
        model = ContactTask
        exclude = []
