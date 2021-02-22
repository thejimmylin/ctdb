from django.contrib import admin

from .models import Log


class LogAdmin(admin.ModelAdmin):

    list_display = ['action', 'app_label', 'model_name', 'data', 'created_at', ]


admin.site.register(Log, LogAdmin)
