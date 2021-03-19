import os
import uuid

from django.core.files.storage import FileSystemStorage


class UUIDFileSystemStorage(FileSystemStorage):

    def generate_filename(self, filename):
        dirname, filename = os.path.split(filename)
        new_filename = str(uuid.uuid4()) + os.path.splitext(filename)[1]
        return os.path.normpath(os.path.join(dirname, new_filename))