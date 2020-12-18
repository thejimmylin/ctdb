from django.db import models


class Diary(models.Model):

    subject = models.CharField(max_length=63)
