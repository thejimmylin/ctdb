from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Log
from diary.models import Diary
from rest_framework import serializers


def now():
    return timezone.localtime(timezone.now())


class DiarySerializer(serializers.ModelSerializer):
    """Using django-rest-framework's serializers is better than json.dumps with custom encoder."""
    class Meta:
        model = Diary
        fields = '__all__'


@receiver(post_save, sender=Diary, dispatch_uid='post_save_diary')
def post_save_diary(sender, instance, created, **kwargs):
    action = 'create' if created else 'update'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data=DiarySerializer(instance).data,
        created_at=now(),
    )


@receiver(post_delete, sender=Diary, dispatch_uid='post_delete_diary')
def post_delete_diary(sender, instance, **kwargs):
    action = 'delete'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data='',
        created_at=now(),
    )
