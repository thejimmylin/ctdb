from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Diary


class DiaryModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'daily_record': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4'}),
            'todo': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4'}),
            'remark': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4'}),
        }
        model = Diary
        exclude = ['created_by']

    def full_clean(self):
        super().full_clean()
        try:
            self.instance.validate_unique()
        except forms.ValidationError:
            self.add_error(field='date', error=_('The diary with this date has already existed.'))


class DiaryCommentModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'readonly': ''}),
            'daily_check': forms.Select(attrs={'readonly': ''}),  # TODO: Make it readonly.
            'daily_record': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4', 'readonly': ''}),
            'todo': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4', 'readonly': ''}),
            'remark': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4', 'readonly': ''}),
        }
        model = Diary
        exclude = ['created_by']

    def full_clean(self):
        super().full_clean()
        try:
            self.instance.validate_unique()
        except forms.ValidationError:
            self.add_error(field='date', error=_('The diary with this date has already existed.'))
