from datetime import timedelta

from django.utils import timezone


def now():
    return timezone.localtime(timezone.now())


def today():
    return timezone.localtime(timezone.now()).date()


def tomorrow():
    return timezone.localtime(timezone.now() + timedelta(days=1)).date()
