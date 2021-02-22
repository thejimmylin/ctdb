from django.db import models
from django.utils.translation import gettext_lazy as _


class Log(models.Model):

    action = models.CharField(
        verbose_name=_('Action'),
        max_length=63,
    )
    app_label = models.CharField(
        verbose_name=_('APP label'),
        max_length=63,
    )
    model_name = models.CharField(
        verbose_name=_('Model name'),
        max_length=63,
    )
    primary_key = models.IntegerField(
        verbose_name=_('Primary key'),
    )
    data = models.TextField(
        verbose_name=_('Data'),
    )
    created_by_username = models.CharField(
        verbose_name=_('Created by username'),
        max_length=63,
    )
