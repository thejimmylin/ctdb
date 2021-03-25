from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import News

admin.site.register(Permission)
admin.site.register(ContentType)
admin.site.register(News)
