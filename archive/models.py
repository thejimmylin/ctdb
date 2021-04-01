from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from .storage import UUIDFileSystemStorage

uuid_file_system_storage = UUIDFileSystemStorage()


class Archive(models.Model):
    archive = models.FileField(storage=uuid_file_system_storage, upload_to='archive')
    name = models.CharField(max_length=255)
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']
        verbose_name = _('Archive')
        verbose_name_plural = _('Archives')

    def __str__(self):
        return self.name

    def get_create_url(self):
        return reverse('archive:archive_create')

    def get_update_url(self):
        return reverse('archive:archive_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('archive:archive_delete', kwargs={'pk': self.pk})
