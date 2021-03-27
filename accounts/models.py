from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils import today


class Profile(models.Model):
    SUPERVISOR_GROUP_NAME = 'SUPERVISORS'

    user = models.OneToOneField(
        verbose_name=_('User'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    staff_code = models.CharField(
        verbose_name=_('Staff code'),
        max_length=63,
        blank=True,
    )
    job_title = models.CharField(
        verbose_name=_('Job title'),
        max_length=63,
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name=_('Phone number'),
        max_length=31,
        blank=True,
    )
    boss = models.ForeignKey(
        verbose_name=_('Boss'),
        to=settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='underling',
    )
    keep_diary = models.BooleanField(
        verbose_name=_('Keep diary'),
        default=False,
    )
    diary_starting_date = models.DateField(
        verbose_name=_('Diary starting date'),
        default=today,
    )

    class Meta():
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def get_displayed_group_names(self):
        group_names = [i.name for i in self.user.groups.filter(groupprofile__is_displayed=True)]
        return group_names

    def get_default_group_name(self):
        group_names = self.get_displayed_group_names()
        if group_names:
            return group_names[0]
        return ''

    def is_supervisor(self):
        return self.user.groups.filter(name=self.SUPERVISOR_GROUP_NAME).exists()


class GroupProfile(models.Model):

    group = models.OneToOneField(
        verbose_name=_('Group'),
        to='auth.Group',
        on_delete=models.CASCADE,
    )
    is_displayed = models.BooleanField(default=False)
    managed_by = models.ForeignKey(
        verbose_name=_('Manager'),
        to=settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='managing_groups',
    )

    class Meta():
        verbose_name = _('Group profile')
        verbose_name_plural = _('Group profiles')

    def __str__(self):
        return f'Profile of group {self.group.name}'
