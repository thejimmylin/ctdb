from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import GroupProfile, Profile

User = get_user_model()


class ProfileAdmin(admin.ModelAdmin):

    def groups_as_str(self, obj):
        return ', '.join(i.name for i in obj.user.groups.all())

    def departments_as_str(self, obj):
        return ', '.join(i.name for i in obj.department.all())

    list_display = ['user', 'groups_as_str', 'departments_as_str', 'staff_code', 'job_title', 'phone_number', 'boss', 'keep_diary', 'diary_starting_date', ]


admin.site.register(Profile, ProfileAdmin)


class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ['group', 'is_displayed', 'managed_by', ]


admin.site.register(GroupProfile, GroupProfileAdmin)
