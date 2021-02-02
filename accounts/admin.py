from django.contrib import admin
from .models import Profile, Department
from django.contrib.auth.models import Permission


class ProfileAdmin(admin.ModelAdmin):

    def departments(self, obj):
        return ', '.join(dep.name for dep in obj.department.all())

    list_display = ['user', 'phone_number', 'departments']


admin.site.register(Profile, ProfileAdmin)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', ]


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Permission)
