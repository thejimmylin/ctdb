from datetime import timedelta

from django.utils import timezone


def now():
    return timezone.localtime(timezone.now())


def today():
    return timezone.localtime(timezone.now()).date()


def tomorrow():
    return timezone.localtime(timezone.now() + timedelta(days=1)).date()


def remove_unnecessary_seperator(s, seperator):
    if s.recipients[-1:] == seperator:
        return s.recipients[:-1]
    return s


def get_clean_objs(s, seperator):
    s = remove_unnecessary_seperator(s, seperator)
    return map(str.strip, s.split(seperator))
