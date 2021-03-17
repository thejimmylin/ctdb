from django.contrib import admin

from .models import Isp, IspGroup, PrefixListUpdateTask

admin.site.register(Isp)
admin.site.register(IspGroup)
admin.site.register(PrefixListUpdateTask)
