from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

User = get_user_model()


@receiver(post_save, sender=User, dispatch_uid='put_profile')
def put_profile(sender, instance, created, **kwargs):
    if kwargs.get('raw', False):
        return
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
