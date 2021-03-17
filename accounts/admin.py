from django.contrib import admin
from django.contrib.auth.models import Permission

from .models import Department, Profile


class ProfileAdmin(admin.ModelAdmin):

    def departments(self, obj):
        return ', '.join(dep.name for dep in obj.department.all())

    list_display = ['user', 'staff_code', 'job_title', 'phone_number', 'departments', 'boss', 'keep_diary', 'diary_starting_date', ]


admin.site.register(Profile, ProfileAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'managed_by', ]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Permission)
