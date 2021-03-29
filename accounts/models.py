from django.conf import settings
from django.contrib.auth.models import Group
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

    def __str__(self):
        return f'Profile of {self.user}'

    def get_plays_outer_roles(self):
        plays = Play.objects.filter(user=self.user)
        plays_outer_roles = plays.values('group_id', 'group__name', 'roles__id', 'roles__name')
        ordered = plays_outer_roles.order_by('group__name', 'roles__name')
        return ordered

    def get_groups_playing_in(self):
        groups_playing_in = Group.objects.filter(play__user=self.user)
        return groups_playing_in

    def get_roles_playing(self):
        roles = Role.objects.filter(play__user=self.user)
        return roles

    def get_displayed_groups(self):
        displayed_groups = self.user.groups.filter(groupprofile__is_displayed=True)
        return displayed_groups

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
    is_displayed = models.BooleanField(
        verbose_name=_('Is displayed'),
        default=False
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
    )

    class Meta():
        verbose_name = _('Group profile')
        verbose_name_plural = _('Group profiles')

    def __str__(self):
        return f'Profile of {self.group}'


class Play(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    group = models.ForeignKey(to='auth.Group', on_delete=models.CASCADE)
    roles = models.ManyToManyField(to='accounts.Role', blank=True)

    class Meta():
        verbose_name = _('Play')
        verbose_name_plural = _('Play')

    def __str__(self):
        roles = ', '.join(str(role) for role in self.roles.all())
        roles = roles if roles else 'a member'
        return f'{self.user}, in group {self.group}, playing {roles}'


class Role(models.Model):
    name = models.CharField(max_length=63)
    codename = models.CharField(max_length=63, unique=True)

    class Meta():
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self):
        return self.name
