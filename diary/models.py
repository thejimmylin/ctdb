from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.utils import today


class Diary(models.Model):
    date = models.DateField(verbose_name=_('Date'), default=today)
    daily_check = models.CharField(
        verbose_name=_('Daily check'),
        max_length=15,
        choices=(
            ('yes', _('Yes')),
            ('no', _('No')),
        ),
        default='no',
    )
    daily_record = models.TextField(verbose_name=_('Daily record'))
    todo = models.TextField(verbose_name=_('To do'), blank=True)
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    comment = models.TextField(verbose_name=_('Comment'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']
        verbose_name = _('Diary')
        verbose_name_plural = _('Diaries')
        unique_together = (('date', 'created_by'), )

    def __str__(self):
        return self.daily_record[:8] + '..'

    def get_create_url(self):
        return reverse('diary:diary_create')

    def get_update_url(self):
        return reverse('diary:diary_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('diary:diary_delete', kwargs={'pk': self.pk})

    def get_clone_url(self):
        return reverse('diary:diary_clone', kwargs={'pk': self.pk})

    def get_comment_url(self):
        return reverse('diary:diary_comment', kwargs={'pk': self.pk})
