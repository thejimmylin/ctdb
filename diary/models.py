from django.db import models


class Person(models.Model):

    department = models.CharField(max_length=63, blank=True)
    job_title = models.CharField(max_length=63, blank=True)
    staff_code = models.CharField(max_length=63, blank=True)
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Diary(models.Model):

    date = models.DateField(null=True)
    todo = models.TextField(null=True)
    daily_record = models.TextField(null=True)
    daily_check = models.BooleanField(default=False)
    remark = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(to='diary.Person', on_delete=models.CASCADE)

    def __str__(self):
        return self.daily_record[:8] + '..'
