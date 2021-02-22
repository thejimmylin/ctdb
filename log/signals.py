from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Log
from diary.models import Diary


@receiver(post_save, sender=Diary, dispatch_uid='log_diary')
def log_diary(sender, instance, created, **kwargs):
    Log.objects.create(
        action='action',
        created_by_username=instance.created_by.username,
    )
