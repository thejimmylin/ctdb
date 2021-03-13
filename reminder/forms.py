from django import forms
from .models import Reminder


class ReminderModelForm(forms.ModelForm):
    class Meta():
        model = Reminder
        exclude = ['created_by']
