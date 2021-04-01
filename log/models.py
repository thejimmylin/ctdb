from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils import now


class Log(models.Model):
    action = models.CharField(verbose_name=_('Action'), max_length=63)
    app_label = models.CharField(verbose_name=_('APP label'), max_length=63)
    model_name = models.CharField(verbose_name=_('Model name'), max_length=63)
    data = models.TextField(verbose_name=_('Data'))
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name=_('Created at'), default=now)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Log')
        verbose_name_plural = _('Logs')
