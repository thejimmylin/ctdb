from django.db import models


class Isp(models.Model):

    name = models.CharField(max_length=63)
    cname = models.CharField(max_length=63)
    upstream_as = models.CharField(max_length=63)
    primary_contact = models.CharField(max_length=63)
    email = models.EmailField(max_length=127)
    phone_number = models.CharField(max_length=63)
    cellphone_number = models.CharField(max_length=63)
    cc = models.CharField(max_length=63)
    remark = models.CharField(max_length=63)
