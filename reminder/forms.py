from django import forms
from .models import Reminder


class ReminderModelForm(forms.ModelForm):

    class Meta():
        widgets = {
            'start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'stop_date': forms.widgets.DateInput(attrs={'type': 'date'}),
        }
        model = Reminder
        exclude = ['created_by']
