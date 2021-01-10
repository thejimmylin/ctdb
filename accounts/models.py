from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):

    user = models.OneToOneField(
        verbose_name=_('User'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    staff_code = models.CharField(max_length=63, blank=True)
    job_title = models.CharField(max_length=63, blank=True)
    phone_number = models.CharField(
        verbose_name=_('Phone number'),
        max_length=31,
        blank=True,
    )

    class Meta():
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
