from django.db import models


class Email(models.Model):

    email = models.EmailField(max_length=127)

    def __str__(self):
        return self.email


class Isp(models.Model):

    name = models.CharField(max_length=63)
    cname = models.CharField(max_length=63)
    upstream_as = models.IntegerField()
    primary_contact = models.CharField(max_length=63)
    to = models.ManyToManyField(to='telecom.Email', related_name='isp_email', blank=True)
    cc = models.ManyToManyField(to='telecom.Email', related_name='isp_cc', blank=True)
    bcc = models.ManyToManyField(to='telecom.Email', related_name='isp_bcc', blank=True)
    telephone = models.CharField(max_length=63, blank=True)
    cellphone = models.CharField(max_length=63, blank=True)
    remark = models.CharField(max_length=63, blank=True)

    def __str__(self):
        return self.name


class IspGroup(models.Model):

    name = models.CharField(max_length=63)
    isps = models.ManyToManyField(to='telecom.Isp')

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
    to = models.ManyToManyField(to='telecom.Email', related_name='contacttask_email', blank=True)
    cc = models.ManyToManyField(to='telecom.Email', related_name='contacttask_cc', blank=True)
    bcc = models.ManyToManyField(to='telecom.Email', related_name='contacttask_bcc', blank=True)
    isp_group = models.ForeignKey(to='telecom.IspGroup', on_delete=models.CASCADE, null=True, blank=True)
    ipv4 = models.BooleanField(default=False)
    ipv6 = models.BooleanField(default=False)
    original_as = models.IntegerField()
    as_path = models.IntegerField()
    remark = models.CharField(max_length=63, blank=True)

    def __str__(self):
        return self.name
