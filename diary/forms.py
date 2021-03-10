from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import Diary


def today():
    return timezone.localtime(timezone.now()).date()


class DiaryModelForm(forms.ModelForm):

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            },
        ),
        label=_('Date'),
        initial=today,
    )
    daily_record = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': _('Daily record'),
                'rows': 4,
            },
        ),
        label=_('Daily record'),
    )
    todo = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': _('To do'),
                'rows': 4,
                'class': 'ckeditor4',
            },
        ),
        label=_('To do'),
        required=False,
    )
    remark = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': _('Remark'),
                'rows': 4,
                'class': 'ckeditor4',
            },
        ),
        label=_('Remark'),
        required=False,
    )

    class Meta():
        model = Diary
        exclude = ['created_by']

    def full_clean(self):
        super().full_clean()
        try:
            self.instance.validate_unique()
        except forms.ValidationError:
            self.add_error(field='date', error=_('The diary with this date has already existed.'))
