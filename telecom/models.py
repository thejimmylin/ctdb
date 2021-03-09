from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import validate_comma_separated_ipv46_address_string  # TODO


class Email(models.Model):
    email = models.EmailField(verbose_name=_('Email'), max_length=127)
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='email_created_by')

    def __str__(self):
        return self.email


class Isp(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=63)
    cname = models.CharField(verbose_name=_('Chinese Name'), max_length=63)
    customer_no = models.CharField(verbose_name=_('Customer No.'), max_length=63)
    upstream_as = models.CharField(verbose_name=_('Upstream AS'), max_length=63)
    primary_contact = models.CharField(verbose_name=_('Primary contact'), max_length=63)
    to = models.ManyToManyField(verbose_name=_('To'), to='telecom.Email', related_name='isp_email', blank=True)
    cc = models.ManyToManyField(verbose_name=_('CC'), to='telecom.Email', related_name='isp_cc', blank=True)
    bcc = models.ManyToManyField(verbose_name=_('BCC'), to='telecom.Email', related_name='isp_bcc', blank=True)
    telephone = models.CharField(verbose_name=_('Telephone'), max_length=63, blank=True)
    cellphone = models.CharField(verbose_name=_('Cellphone'), max_length=63, blank=True)
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def to_as_str(self):
        return ';\n'.join(instance.email for instance in self.to.all())

    def cc_as_str(self):
        return ';\n'.join(instance.email for instance in self.cc.all())

    def bcc_as_str(self):
        return ';\n'.join(instance.email for instance in self.bcc.all())


class IspGroup(models.Model):

    name = models.CharField(verbose_name=_('Name'), max_length=63)
    isps = models.ManyToManyField(verbose_name=_('ISPs'), to='telecom.Isp')
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def isps_as_str(self):
        return ',\n'.join(instance.name for instance in self.isps.all())


class PrefixListUpdateTask(models.Model):

    update_type = models.CharField(
        verbose_name=_('Update type'),
        max_length=64,
        choices=(
            ('add ip-prefix', 'Add IP-prefix'),
            ('add as', 'Add AS'),
            ('add route', 'Add Route'),
        )
    )
    isps = models.ManyToManyField(verbose_name=_('ISPs'), to='telecom.Isp', blank=True)
    isp_groups = models.ManyToManyField(verbose_name=_('ISP groups'), to='telecom.IspGroup', blank=True)
    configs = models.TextField(verbose_name=_('Configs'))
    """
    example:

    configs = [
        {
            "original_as": "16999",
            "as_path": "16999-888-777",
            "ip_network": ["100.88.77.0/24", "100.88.78.0/24", "2129:0375:0718:226d:0:0:0:0/64"]
        },
        {
            "original_as": "16888",
            "as_path": "16888-666-777",
            "ip_network": ["100.99.88.0/24", "c44d:0fda:5e07:f12d:0:0:0:0/64"]
        }
    ]
    """
    remark = models.TextField(verbose_name=_('Remark'), blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.update_type} {self.isps} {self.isp_groups}'

    def isps_as_str(self):
        return ',\n'.join(instance.name for instance in self.isps.all())

    def isp_group_as_str(self):
        return ',\n'.join(instance.name for instance in self.isp_groups.all())
