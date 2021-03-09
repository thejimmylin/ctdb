from django import forms

from .models import Email, Isp, IspGroup, ContactTask


class EmailModelForm(forms.ModelForm):
    class Meta():
        model = Email
        exclude = ['created_by', ]


class IspModelForm(forms.ModelForm):
    class Meta():
        model = Isp
        exclude = ['created_by', ]


class IspGroupModelForm(forms.ModelForm):
    class Meta():
        model = IspGroup
        exclude = ['created_by', ]


class ContactTaskModelForm(forms.ModelForm):
    class Meta():
        model = ContactTask
        exclude = ['created_by', ]
