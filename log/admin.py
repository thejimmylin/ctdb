from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):

    list_display = ['action', 'created_by_username', ]


admin.site.register(Log, LogAdmin)
