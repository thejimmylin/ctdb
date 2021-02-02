from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class Diary(models.Model):
    date = models.DateField(verbose_name=_('Date'), null=True)
    daily_check = models.CharField(verbose_name=_('Daily check'), max_length=15)
    daily_record = models.TextField(verbose_name=_('Daily record'), null=True)
    todo = models.TextField(verbose_name=_('To do'), null=True, blank=True)
    remark = models.TextField(verbose_name=_('Remark'), null=True, blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        verbose_name = _('Diary')
        verbose_name_plural = _('Diaries')
        unique_together = (('date', 'created_by'), )

    def __str__(self):
        return self.daily_record[:8] + '..'


class Preference(models.Model):
    pass
