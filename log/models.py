from django.db import models
from django.utils.translation import gettext_lazy as _


class Log(models.Model):

    action = models.CharField(verbose_name=_('Action'), max_length=63)
    app_label = models.CharField(verbose_name=_('APP label'), max_length=63)
    model_name = models.CharField(verbose_name=_('Model name'), max_length=63)
    data = models.JSONField(verbose_name=_('Data'), default=dict)
    created_at = models.DateTimeField(verbose_name=_('Created at'))
