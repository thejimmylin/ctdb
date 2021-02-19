from django.contrib import admin

from .models import Day


class DayAdmin(admin.ModelAdmin):

    list_display = ['id', 'date', 'is_holiday', ]
    list_editable = ['date', 'is_holiday', ]


admin.site.register(Day, DayAdmin)
