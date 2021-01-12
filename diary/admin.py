from django.contrib import admin
from .models import Diary


class DiaryAdmin(admin.ModelAdmin):

    list_display = ['date', 'todo', 'daily_record', 'daily_check']


admin.site.register(Diary, DiaryAdmin)
