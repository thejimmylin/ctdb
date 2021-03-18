from django.conf import settings
from django.db import models

from .storage import UUIDFileSystemStorage


uuid_file_system_storage = UUIDFileSystemStorage()


class Archive(models.Model):
    archive = models.FileField(storage=uuid_file_system_storage, upload_to='archive')
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
