from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Day


class DayAdmin(admin.ModelAdmin):

    def href(self, obj):
        return _('See more..')

    list_display_links = ['href']
    list_display = ['date', 'is_holiday', 'href']
    list_editable = ['date', 'is_holiday', ]


admin.site.register(Day, DayAdmin)
