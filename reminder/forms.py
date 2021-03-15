from django import forms
from .models import Reminder
from django.utils.translation import gettext_lazy as _


class ReminderModelForm(forms.ModelForm):
    class Meta():
        model = Reminder
        exclude = ['created_by']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'stop_date': forms.DateInput(attrs={'type': 'date'}),
            'advanced_policy': forms.Textarea(attrs={
                'rows': 10,
                'placeholder': _(
                    'Please enter one or more specified dates separated by "," and '
                    'the date format must be yyyy-mm-dd. For example:\n'
                    '\n'
                    '2021-03-16,\n'
                    '2021-03-29,\n'
                    '2021-04-01\n'
                ),
            }),
            'recipients': forms.Textarea(attrs={
                'rows': 10,
                'placeholder': _(
                    'Please enter one or more Email separated by ";".\n'
                    'For example:\n'
                    '\n'
                    'example1@chief.com.tw;\n'
                    'example2@google.com;\n'
                ),
            }),
        }
