from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.utils import today, tomorrow
from core.validators import (validate_comma_seperated_date_string,
                             validate_semicolon_seperated_email_string)


class Reminder(models.Model):
    POLICY = [
        (_('Common'), (
            ('on weekdays', _('On weekdays')),
            ('daily', _('Daily')),
            ('once', _('Once')),
            ('every monday', _('Every Monday')),
            ('every tuesday', _('Every Tuesday')),
            ('every wednesday', _('Every Wednesday')),
            ('every thursday', _('Every Thursday')),
            ('every friday', _('Every Friday')),
            ('every saturday', _('Every Saturday')),
            ('every sunday', _('Every Sunday')),
        )
        ),
        (_('Specific'), (
            ('specified dates', _('Specified dates')),
        )
        ),
    ]
    is_active = models.BooleanField(verbose_name=_('Is active'), default=True)
    event = models.CharField(verbose_name=_('Event'), max_length=63)
    policy = models.CharField(verbose_name=_('Policy'), max_length=63, choices=POLICY, default='on weekdays')
    start_at = models.DateField(verbose_name=_('Start at'), default=today, blank=True, null=True)
    end_at = models.DateField(verbose_name=_('End at'), default=tomorrow, blank=True, null=True)
    specified_dates = models.TextField(verbose_name=_('Specified dates'), blank=True, validators=[validate_comma_seperated_date_string])
    email_subject = models.CharField(verbose_name=_('Email subject'), max_length=63)
    email_content = models.TextField(verbose_name=_('Email content'), blank=True)
    recipients = models.TextField(
        verbose_name=_('Recipients'),
        help_text=_('Use ";" to seperate multiple recipient.'),
        validators=[validate_semicolon_seperated_email_string],
    )
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_create_url(self):
        return reverse('reminder:reminder_create')

    def get_update_url(self):
        return reverse('reminder:reminder_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('reminder:reminder_delete', kwargs={'pk': self.pk})

    def get_send_email_url(self):
        return reverse('reminder:reminder_send_email', kwargs={'pk': self.pk})
