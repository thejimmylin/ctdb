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
    keep_diary = models.BooleanField(
        verbose_name=_('Keep diary'),
        default=False,
    )
    diary_starting_date = models.DateField(
        verbose_name=_('Diary starting date'),
        default=today,
    )
    activated_role = models.ForeignKey(
        to='auth.Group',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

    def __str__(self):
        return f'Profile of {self.user}'

    def is_supervisor_of(self, another_user):
        """
        Given a `another_user`. If this user is supervisor of `another_user`, return True,
        else return False.
        """
        role = self.activated_role
        if not role:
            return False
        supervise_roles = role.groupprofile.supervise_roles.all()
        if not supervise_roles:
            return False
        if not another_user.groups.filter(pk__in=supervise_roles):
            return False
        return True


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

    class Meta:
        verbose_name = _('Group profile')
        verbose_name_plural = _('Group profiles')

    def __str__(self):
        return f'Profile of {self.group}'
