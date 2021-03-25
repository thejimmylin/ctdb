import json

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from rest_framework import serializers

from diary.models import Diary

from .models import Log


class DiarySerializer(serializers.ModelSerializer):
    """
    Using django-rest-framework's serializers is better than json.dumps with custom encoder.
    """
    class Meta:
        model = Diary
        fields = '__all__'


@receiver(post_save, sender=Diary, dispatch_uid='post_save_diary')
def post_save_diary(sender, instance, created, **kwargs):
    action = 'CREATE' if created else 'UPDATE'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    created_by = instance.created_by if hasattr(instance, 'created_by') else None
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data=json.dumps(DiarySerializer(instance).data, ensure_ascii=False),
        created_by=created_by,
    )


@receiver(post_delete, sender=Diary, dispatch_uid='post_delete_diary')
def post_delete_diary(sender, instance, **kwargs):
    action = 'DELETE'
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    created_by = instance.created_by if hasattr(instance, 'created_by') else None
    Log.objects.create(
        action=action,
        app_label=app_label,
        model_name=model_name,
        data=json.dumps(DiarySerializer(instance).data, ensure_ascii=False),
        created_by=created_by,
    )
