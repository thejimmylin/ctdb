from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import GroupProfile, Profile, Play, Role

User = get_user_model()


class ProfileAdmin(admin.ModelAdmin):

    def groups_as_str(self, obj):
        return ', '.join(i.name for i in obj.user.groups.all())

    list_display = ['user', 'groups_as_str', 'staff_code', 'job_title', 'phone_number', 'boss', 'keep_diary', 'diary_starting_date']


admin.site.register(Profile, ProfileAdmin)


class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ['group', 'managed_by', 'is_displayed', 'is_department', 'parent_department']


admin.site.register(GroupProfile, GroupProfileAdmin)


class PlayAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'group']


admin.site.register(Play, PlayAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['__str__']


admin.site.register(Role, RoleAdmin)
