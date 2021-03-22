from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import GroupProfile, Profile

User = get_user_model()


@receiver(post_save, sender=User, dispatch_uid='put_profile')
def put_profile(sender, instance, created, **kwargs):
    if kwargs.get('raw', False):
        return
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=Group, dispatch_uid='put_group_profile')
def put_group_profile(sender, instance, created, **kwargs):
    if kwargs.get('raw', False):
        return
    if created:
        GroupProfile.objects.create(group=instance)
    instance.groupprofile.save()
