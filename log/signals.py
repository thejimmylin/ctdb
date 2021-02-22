from django.db.models.signals import post_save, post_delete
from django.forms.models import model_to_dict
from django.dispatch import receiver
from .models import Log
from diary.models import Diary


@receiver(post_save, sender=Diary, dispatch_uid='post_save_diary')
def post_save_diary(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    Log.objects.create(
        action=action,
        app_label=instance._meta.app_label,
        model_name=instance._meta.model_name,
        primary_key=instance.pk,
        data=str(model_to_dict(instance)),
        created_by_username=instance.created_by.username,
    )


@receiver(post_delete, sender=Diary, dispatch_uid='post_delete_diary')
def post_delete_diary(sender, instance, **kwargs):
    action = 'delete'
    Log.objects.create(
        action=action,
        app_label=instance._meta.app_label,
        model_name=instance._meta.model_name,
        primary_key=instance.pk,
        data=str(model_to_dict(instance)),
        created_by_username=instance.created_by.username,
    )
