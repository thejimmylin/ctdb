from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.validators import (validate_comma_separated_prefix_list_string,
                             validate_semicolon_seperated_email_string)


class Isp(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=63)
    cname = models.CharField(verbose_name=_('Chinese Name'), max_length=63)
    customer_no = models.CharField(verbose_name=_('Customer No.'), max_length=63)
    upstream_as = models.CharField(verbose_name=_('Upstream AS'), max_length=63)
    primary_contact = models.CharField(verbose_name=_('Primary contact'), max_length=63)
    to = models.TextField(verbose_name=_('To'), blank=True, validators=[validate_semicolon_seperated_email_string, ])
    cc = models.TextField(verbose_name=_('CC'), blank=True, validators=[validate_semicolon_seperated_email_string, ])
    bcc = models.TextField(verbose_name=_('BCC'), blank=True, validators=[validate_semicolon_seperated_email_string, ])
    telephone = models.CharField(verbose_name=_('Telephone'), max_length=63, blank=True)
    cellphone = models.CharField(verbose_name=_('Cellphone'), max_length=63, blank=True)
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        ordering = ['-id']
        verbose_name = _('ISP')
        verbose_name_plural = _('ISPs')

    def __str__(self):
        return self.name

    def get_create_url(self):
        return reverse('telecom:isp_create')

    def get_update_url(self):
        return reverse('telecom:isp_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('telecom:isp_delete', kwargs={'pk': self.pk})


class IspGroup(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=63)
    isps = models.ManyToManyField(verbose_name=_('ISPs'), to='telecom.Isp')
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        ordering = ['-id']
        verbose_name = _('ISP group')
        verbose_name_plural = _('ISP groups')

    def __str__(self):
        return self.name

    def get_create_url(self):
        return reverse('telecom:ispgroup_create')

    def get_update_url(self):
        return reverse('telecom:ispgroup_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('telecom:ispgroup_delete', kwargs={'pk': self.pk})


class PrefixListUpdateTask(models.Model):
    update_type = models.CharField(
        verbose_name=_('Update type'),
        max_length=63,
        choices=(
            ('add prefix-list', _('Add prefix-list')),
            ('add as', _('Add AS')),
            ('add route', _('Add Route')),
        )
    )
    isps = models.ManyToManyField(verbose_name=_('ISPs'), to='telecom.Isp', blank=True)
    isp_groups = models.ManyToManyField(verbose_name=_('ISP groups'), to='telecom.IspGroup', blank=True)
    origin_as = models.CharField(verbose_name=_('Origin AS'), max_length=63)
    as_path = models.CharField(verbose_name=_('AS path'), max_length=63)
    prefix_list = models.TextField(verbose_name=_('Prefix-list'), validators=[validate_comma_separated_prefix_list_string, ])
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta():
        ordering = ['-id']
        verbose_name = _('Prefix-list update task')
        verbose_name_plural = _('Prefix-list update tasks')

    def get_create_url(self):
        return reverse('telecom:prefixlistupdatetask_create')

    def get_update_url(self):
        return reverse('telecom:prefixlistupdatetask_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('telecom:prefixlistupdatetask_delete', kwargs={'pk': self.pk})
