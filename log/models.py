from django.db import models
from django.utils.translation import gettext_lazy as _


class Log(models.Model):

    action = models.CharField(
        verbose_name=_('Action'),
        max_length=63,
    )
    created_by_username = models.CharField(
        verbose_name=_('Created by username'),
        max_length=63,
    )
