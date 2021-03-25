from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.conf import settings
from core.utils import now


class News(models.Model):

    title = models.CharField(verbose_name=_('Title'), max_length=31)
    content = models.TextField(verbose_name=_('Content'))
    at = models.DateTimeField(verbose_name=_('at'), default=now)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        ordering = ['-at']
        verbose_name = _('New')
        verbose_name_plural = _('News')

    def get_create_url(self):
        return reverse('news_create')

    def get_update_url(self):
        return reverse('news_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('news_delete', kwargs={'pk': self.pk})
