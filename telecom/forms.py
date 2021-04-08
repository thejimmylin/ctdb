from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Isp, IspGroup, PrefixListUpdateTask


class IspModelForm(forms.ModelForm):
    to = forms.CharField(
        label=_('To'),
        widget=forms.Textarea(
            attrs={
                'placeholder': _(
                    'Please enter one or more Email separated by ";".\n'
                    'For example:\n'
                    '\n'
                    'example1@chief.com.tw;\n'
                    'example2@google.com;\n'
                ),
                'row': 10
            }
        ),
    )
    cc = forms.CharField(
        label=_('CC'),
        widget=forms.Textarea(
            attrs={
                'placeholder': _(
                    'Please enter one or more Email separated by ";".\n'
                    'For example:\n'
                    '\n'
                    'example1@chief.com.tw;\n'
                    'example2@google.com;\n'
                ),
                'row': 10
            }
        ),
        required=False
    )
    bcc = forms.CharField(
        label=_('BCC'),
        widget=forms.Textarea(
            attrs={
                'placeholder': _(
                    'Please enter one or more Email separated by ";".\n'
                    'For example:\n'
                    '\n'
                    'example1@chief.com.tw;\n'
                    'example2@google.com;\n'
                ),
                'row': 10
            }
        ),
        required=False
    )

    class Meta:
        model = Isp
        exclude = ['created_by', ]


class IspGroupModelForm(forms.ModelForm):

    class Meta:
        model = IspGroup
        exclude = ['created_by', ]


class PrefixListUpdateTaskModelForm(forms.ModelForm):
    prefix_list = forms.CharField(
        label=_('Prefix-list'),
        widget=forms.Textarea(
            attrs={
                'placeholder': _(
                    'Please enter a prefix-list. For example:\n'
                    '\n'
                    '100.100.100.100/24,\n'
                    '100.100.200.100/22 le 24,\n'
                ),
                'rows': 12
            }
        ),
    )
    related_ticket = forms.CharField(
        label=_('Related ticket'),
        widget=forms.Textarea(
            attrs={
                'placeholder': _(
                    'Please enter related tickets of this update task, if there is any.'
                ),
                'rows': 3
            }
        )
    )

    class Meta:
        model = PrefixListUpdateTask
        exclude = ['created_by', ]
