from django.contrib import admin
from .models import Email, Isp, IspGroup, ContactTask


admin.site.register(Email)
admin.site.register(Isp)
admin.site.register(IspGroup)
admin.site.register(ContactTask)
