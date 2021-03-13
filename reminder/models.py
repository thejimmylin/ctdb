from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils import today


class Reminder(models.Model):
    PERIOD = [
        ('once', _('Once')),
        ('daily', _('Daily')),
        ('on weekdays', _('On Weekdays')),
        ('every 7 days', _('Every 7 days')),
        ('1st of every month', _('1st of every month')),
        ('2nd of every month', _('2nd of every month')),
        ('3nd of every month', _('3rd of every month')),
    ]
    PERIOD += [
        (f'{n}th of every month', _('%(n)sth of every month'))
        for n in range(4, 32)
    ]
    event_type = models.CharField(verbose_name=_('Event type'), max_length=63)
    event = models.CharField(verbose_name=_('Event'), max_length=63)
    start_date = models.DateField(verbose_name=_('Start date'), default=today)
    stop_date = models.DateField(verbose_name=_('Stop date'), default=today)
    period = models.CharField(verbose_name=_('Period'), max_length=63, choices=PERIOD, default='on weekdays')
    subject = models.CharField(verbose_name=_('Subject'), max_length=63)
    email_subject = models.TextField(verbose_name=_('email suject'))
    recipients = models.TextField(verbose_name=_('Recipients'), help_text=_('Use ";" to seperate multiple recipient.'))
