from django.conf import settings
from django.contrib.auth.models import Group
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
    keep_diary = models.BooleanField(
        verbose_name=_('Keep diary'),
        default=False,
    )
    diary_starting_date = models.DateField(
        verbose_name=_('Diary starting date'),
        default=today,
    )

    def get_roles(self):
        return self.user.groups.filter(groupprofile__is_role=True)

    def get_available_roles(self):
        return self.user.groups.filter(groupprofile__is_role=True, groupprofile__is_displayed=True)

    def get_default_role(self):
        return self.get_available_roles().first()

    class Meta():
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f'Profile of {self.user}'


def get_role(session, user):
    role = session.get('role', {})
    pk = role.get('pk', 0)
    try:
        pk = int(role.get('pk', 0))
    except ValueError:
        return None
    try:
        role = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return None
    if role not in user.profile.get_available_roles():
        return None
    return role


class GroupProfile(models.Model):
    group = models.OneToOneField(
        verbose_name=_('Group'),
        to='auth.Group',
        on_delete=models.CASCADE,
    )
    is_role = models.BooleanField(
        verbose_name=_('Is role'),
        default=False
    )
    is_displayed = models.BooleanField(
        verbose_name=_('Is displayed'),
        default=False
    )
    supervise_roles = models.ManyToManyField(
        verbose_name=_('Supervise roles'),
        to='auth.Group',
        blank=True,
        related_name='supervised_by_roles',
        limit_choices_to={'groupprofile__is_role': True},
    )
    is_department = models.BooleanField(
        verbose_name=_('Is department'),
        default=False
    )
    parent_department = models.ForeignKey(
        verbose_name=_('Parent Department'),
        to='auth.Group',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='child_departments',
        limit_choices_to={'groupprofile__is_department': True},
    )

    class Meta():
        verbose_name = _('Group profile')
        verbose_name_plural = _('Group profiles')

    def __str__(self):
        return f'Profile of {self.group}'
