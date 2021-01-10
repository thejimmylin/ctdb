from django.db import models
from django.conf import settings


class Diary(models.Model):

    date = models.DateField(null=True)
    todo = models.TextField(null=True)
    daily_record = models.TextField(null=True)
    daily_check = models.BooleanField(default=False)
    remark = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.daily_record[:8] + '..'
