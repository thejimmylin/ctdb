from django.db.models.signals import post_save, post_delete
from django.forms.models import model_to_dict
from django.dispatch import receiver
from django.utils import timezone
from .models import Log
from diary.models import Diary


def now():
    return timezone.localtime(timezone.now())


def create_log(action, instance):
    instance_dict = model_to_dict(instance)
    app_label = instance._meta.app_label
    model_name = instance._meta.model_name
    primary_key = instance_dict.pop('id')
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        primary_key=primary_key,
        body=str(instance_dict),
        created_at=now(),
    )


@receiver(post_save, sender=Diary, dispatch_uid='post_save_diary')
def post_save_diary(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    create_log(action=action, instance=instance)


@receiver(post_delete, sender=Diary, dispatch_uid='post_delete_diary')
def post_delete_diary(sender, instance, **kwargs):
    action = 'delete'
    create_log(action=action, instance=instance)
