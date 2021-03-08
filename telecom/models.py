from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from .validators import validate_comma_separated_ipv46_address_string  # TODO


class Email(models.Model):

    email = models.EmailField(max_length=127)
    remark = models.TextField(blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='email_created_by')

    def __str__(self):
        return self.email


class Isp(models.Model):

    name = models.CharField(max_length=63)
    cname = models.CharField(max_length=63)
    customer_no = models.CharField(max_length=63)
    upstream_as = models.IntegerField()
    primary_contact = models.CharField(max_length=63)
    to = models.ManyToManyField(to='telecom.Email', related_name='isp_email', blank=True)
    cc = models.ManyToManyField(to='telecom.Email', related_name='isp_cc', blank=True)
    bcc = models.ManyToManyField(to='telecom.Email', related_name='isp_bcc', blank=True)
    telephone = models.CharField(max_length=63, blank=True)
    cellphone = models.CharField(max_length=63, blank=True)
    remark = models.TextField()
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class IspGroup(models.Model):

    name = models.CharField(max_length=63)
    isps = models.ManyToManyField(to='telecom.Isp')
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ContactTask(models.Model):

    contact_type = models.CharField(
        max_length=64,
        choices=(
            ('add ip-prefix', 'Add IP-prefix'),
            ('add as', 'Add AS'),
            ('add route', 'Add Route'),
        )
    )
    to_isp = models.ManyToManyField(to='telecom.Isp', blank=True)
    to_isp_group = models.ManyToManyField(to='telecom.IspGroup', blank=True)
    ip_network = models.TextField()
    """
    example:

    task_configs = [
        {
            "original_as": "16999",
            "as_path": "16999-888-777",
            "ip_network": ["100.88.77.0/24", "100.88.78.0/24", "2129:0375:0718:226d:0:0:0:0/64"]
        },
        {
            "original_as": "16888",
            "as_path": "16888-666-777",
            "ip_network": ["100.99.88.0/24", "c44d:0fda:5e07:f12d:0:0:0:0/64"]
        },
    ]
    """
    remark = models.TextField(blank=True)
    created_by = models.ForeignKey(verbose_name=_('Created by'), to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.contact_type} {self.to_isp}'
