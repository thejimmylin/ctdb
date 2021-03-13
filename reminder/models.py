from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils import today
from django.urls import reverse


class Reminder(models.Model):
    PERIOD = [
        ('once', _('Once')),
        ('daily', _('Daily')),
        ('on weekdays', _('On Weekdays')),
        ('every 7 days', _('Every 7 days')),
        ('1st of every month', _('1st of every month')),
        ('2nd of every month', _('2nd of every month')),
        ('3nd of every month', _('3rd of every month')),
    ] + [
        ('%(n)sth of every month' % {'n': n}, _('%(n)sth of every month') % {'n': n})
        for n in range(4, 32)
    ]
    event = models.CharField(verbose_name=_('Event'), max_length=63)
    start_date = models.DateField(verbose_name=_('Start date'), default=today)
    stop_date = models.DateField(verbose_name=_('Stop date'), default=today)
    period = models.CharField(verbose_name=_('Period'), max_length=63, choices=PERIOD, default='on weekdays')
    email_subject = models.CharField(verbose_name=_('Email subject'), max_length=63)
    email_content = models.TextField(verbose_name=_('Email content'))
    recipients = models.TextField(verbose_name=_('Recipients'), help_text=_('Use ";" to seperate multiple recipient.'))
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def get_create_url(self):
        return reverse('reminder:reminder_create')

    def get_update_url(self):
        return reverse('reminder:reminder_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('reminder:reminder_delete', kwargs={'pk': self.pk})
