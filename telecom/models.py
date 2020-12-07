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
    email = models.EmailField(max_length=127)
    cc = models.CharField(max_length=63)
    telephone = models.CharField(max_length=63)
    cellphone = models.CharField(max_length=63)
    remark = models.CharField(max_length=63)
