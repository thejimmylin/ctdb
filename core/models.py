from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class News(models.Model):

    title = models.CharField(max_length=31)
    content = models.TextField()

    class Meta():
        ordering = ['-id']
        verbose_name = _('New')
        verbose_name_plural = _('News')

    def get_create_url(self):
        return reverse('news_create')

    def get_update_url(self):
        return reverse('news_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('news_delete', kwargs={'pk': self.pk})
