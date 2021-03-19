from django.db import models
from django.utils.translation import gettext_lazy as _


class Day(models.Model):

    date = models.DateField(
        verbose_name=_('Date'),
        blank=True,
        null=True,
    )
    is_holiday = models.BooleanField(
        verbose_name=_('Is holiday'),
        default=False,
    )

    class Meta():
        ordering = ['date']
        verbose_name = _('Day')
        verbose_name_plural = _('Days')

    def __str__(self):
        day_type_string = '"H"' if self.is_holiday else '"W"'
        return f'{self.date} {day_type_string}'
