from datetime import timedelta

from django.utils import timezone


def now():
    """
    Return a datetime.datetime object of now with timezone.localtime computed.
    """
    return timezone.localtime(timezone.now())


def today():
    """
    Return a datetime.date object of today with timezone.localtime computed.
    """
    return timezone.localtime(timezone.now()).date()


def tomorrow():
    """
    Return a datetime.date object of tomorrow with timezone.localtime computed.
    """
    return timezone.localtime(timezone.now() + timedelta(days=1)).date()


def date_range(start_date, end_date):
    """
    Given two datetime.date or datetime.datetime, retrun a date range.
    """
    days = (end_date - start_date).days
    date_range = [start_date + timedelta(n) for n in range(days)]
    return date_range


def remove_unnecessary_seperator(s, seperator):
    if s[-1:] == seperator:
        return s[:-1]
    return s
