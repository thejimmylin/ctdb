from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import GroupProfile, Profile, Play, Role

User = get_user_model()


class ProfileAdmin(admin.ModelAdmin):

    def get_user_groups(self, obj):
        return ', '.join(str(group) for group in obj.user.groups.all())

    list_display = ['__str__', 'user', 'get_user_groups', 'staff_code', 'job_title', 'phone_number', 'boss', 'keep_diary', 'diary_starting_date']


admin.site.register(Profile, ProfileAdmin)


class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'group', 'is_displayed', 'is_department', 'parent_department']


admin.site.register(GroupProfile, GroupProfileAdmin)


class PlayAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'group', 'get_roles']

    def get_roles(self, obj):
        roles = ', '.join(str(role) for role in obj.roles.all())
        return roles


admin.site.register(Play, PlayAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'codename']


admin.site.register(Role, RoleAdmin)
