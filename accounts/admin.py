from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import GroupProfile, Profile

User = get_user_model()


class ProfileAdmin(admin.ModelAdmin):
    def get_user_groups(self, obj):
        return ', '.join(str(group) for group in obj.user.groups.all())

    list_display = ['__str__', 'get_user_groups', 'staff_code', 'job_title', 'phone_number', 'keep_diary', 'diary_starting_date']
    list_editable = ['staff_code', 'job_title', 'phone_number', 'keep_diary', 'diary_starting_date']


admin.site.register(Profile, ProfileAdmin)


class GroupProfileAdmin(admin.ModelAdmin):
    def get_users(self, obj):
        return ', '.join(str(user) for user in obj.group.user_set.all())

    list_display = ['__str__', 'get_users', 'is_department', 'parent_department', 'is_role', 'is_displayed']
    list_editable = ['is_department', 'is_role', 'is_displayed']


admin.site.register(GroupProfile, GroupProfileAdmin)
