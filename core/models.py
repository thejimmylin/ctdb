from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):

    title = models.CharField(max_length=31)
    content = models.TextField()

    class Meta():
        ordering = ['-id']
        verbose_name = _('New')
        verbose_name_plural = _('News')
