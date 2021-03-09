from django.contrib import admin
from .models import Email, Isp, IspGroup, PrefixListUpdateTask


admin.site.register(Email)
admin.site.register(Isp)
admin.site.register(IspGroup)
admin.site.register(PrefixListUpdateTask)
