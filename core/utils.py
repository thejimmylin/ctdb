from django.utils import timezone


def today():
    return timezone.localtime(timezone.now()).date()
