from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from core.utils import today


class Profile(models.Model):

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
    department = models.ManyToManyField(
        to='Department',
        max_length=64,
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

    def get_available_roles(self):
        roles = [i.name for i in self.user.groups.filter(is_displayed=True)]
        return roles

    def get_default_role(self):
        roles = self.get_available_roles()
        if roles:
            return roles[0]
        return ''


class Department(models.Model):

    name = models.CharField(
        verbose_name=_('Name'),
        unique=True,
        max_length=32,
    )
    managed_by = models.ForeignKey(
        verbose_name=_('Boss'),
        to=settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='managing',
    )

    class Meta():
        verbose_name = _('Department')
        verbose_name_plural = _('Departments')

    def __str__(self):
        return self.name


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
