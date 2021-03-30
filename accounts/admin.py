from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import GroupProfile, Profile

User = get_user_model()


class ProfileAdmin(admin.ModelAdmin):

    def get_user_groups(self, obj):
        return ', '.join(str(group) for group in obj.user.groups.all())

    list_display = ['__str__', 'user', 'get_user_groups', 'staff_code', 'job_title', 'phone_number', 'boss', 'keep_diary', 'diary_starting_date']


admin.site.register(Profile, ProfileAdmin)


class GroupProfileAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'group', 'is_department', 'parent_department']


admin.site.register(GroupProfile, GroupProfileAdmin)
