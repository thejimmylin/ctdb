import uuid

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       UsernameField)
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

from .models import Profile

User = get_user_model()


class SignUpWithEmailForm(forms.ModelForm):

    email = forms.EmailField(
        label=_('Email'),
        required=True,
        max_length=63,
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
            },
        ),
        help_text=_('Email cannot be changed after setting.')
    )

    field_order = ['username', 'email', 'first_name', 'last_name']

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {
            'username': '',
        }

    def __init__(self, email_endswith_strings=[], email_cant_endswith_strings=[], *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.email_endswith_strings = email_endswith_strings
        self.email_cant_endswith_strings = email_cant_endswith_strings

    def clean_email(self):
        email = self.cleaned_data['email']
        email_endswith_valid_string = False if self.email_endswith_strings else True
        for email_endswith_string in self.email_endswith_strings:
            if email.endswith(email_endswith_string):
                email_endswith_valid_string = True
                break
        if not email_endswith_valid_string:
            self.add_error(
                'email',
                ValidationError(
                    _('The Email address must end with %(join_email_endswith_strings)s.'),
                    params={'join_email_endswith_strings': ', '.join(self.email_endswith_strings)},
                    code='invalid'
                )
            )
        email_endswith_invalid_string = False
        for email_cant_endswith_string in self.email_cant_endswith_strings:
            if email.endswith(email_cant_endswith_string):
                email_endswith_invalid_string = True
                break
        if email_endswith_invalid_string:
            self.add_error(
                'email',
                ValidationError(
                    _('The Email address must not end with %(join_email_cant_endswith_strings)s.'),
                    params={'join_email_cant_endswith_strings': ', '.join(self.email_cant_endswith_strings)},
                    code='invalid'
                )
            )
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    _('A user with this Email already exists.'),
                    code='invalid'
                )
            )
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        random_uuid_password = uuid.uuid4()
        user.set_password(str(random_uuid_password))
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        subject = '[TDB] You have created an account.'
        message = (
            f'Hi {username},\n'
            '\n'
            'You have created a new account on TDB.\n'
            'You could login and change it on TDB later.\n'
            '\n'
            f'Your account: {username}\n'
            f'Your password: {random_uuid_password}\n'
            '\n'
            'Sincerely,\n'
            'TDB\n'
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
            fail_silently=False,
        )
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    """
    Extend AuthenticationForm and disable the autofocus on field username.
    """
    username = UsernameField(widget=forms.TextInput())


class ProfileForm(forms.ModelForm):

    username = forms.CharField(
        label=_('Username'),
        max_length=63,
        required=False,
    )
    email = forms.EmailField(
        label=_('Email'),
        max_length=63,
        widget=forms.EmailInput(
            attrs={
                'placeholder': _('Email'),
            }
        ),
        required=False,
    )
    staff_code = forms.CharField(
        label=_('Staff code'),
        max_length=63,
        required=False,
    )
    job_title = forms.CharField(
        label=_('Job title'),
        max_length=63,
        required=False,
    )
    activated_role = forms.ModelChoiceField(
        label=_('Activated role'),
        required=False,
        queryset=Group.objects.all(),
    )
    keep_diary = forms.BooleanField(
        label=_('Keep diary'),
        required=False,
        disabled=True,
    )
    diary_starting_date = forms.DateField(
        label=_('Diary starting date'),
        required=False,
        disabled=True,
    )

    class Meta:
        model = Profile
        fields = ['username', 'email', 'staff_code', 'job_title', 'phone_number', 'activated_role', 'keep_diary', 'diary_starting_date', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].initial = self.instance.user.username
        self.fields['email'].initial = self.instance.user.email
        self.fields['activated_role'].queryset = self.instance.user.groups.filter(groupprofile__is_role=True, groupprofile__is_displayed=True)
        if self.instance.user.username:
            self.fields['username'].disabled = True
        if self.instance.user.email:
            self.fields['email'].disabled = True

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.user.username = self.cleaned_data['username']
        instance.user.email = self.cleaned_data['email']
        instance.user.phone_number = self.cleaned_data['phone_number']
        if commit:
            instance.save()
        return instance


class EmailValidationOnForgotPasswordForm(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    _('No user registering with this Email.'),
                    code='invalid'
                )
            )
        return email
