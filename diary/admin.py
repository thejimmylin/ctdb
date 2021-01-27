from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Diary


class DiaryAdmin(admin.ModelAdmin):

    list_display = ['date', 'todo', 'daily_record', 'daily_check', 'created_by']


admin.site.register(Diary, DiaryAdmin)
admin.site.register(Permission)
