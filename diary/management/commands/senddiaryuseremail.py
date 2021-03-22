from datetime import timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.management.base import BaseCommand

from core.utils import today
from day.models import Day
from diary.models import Diary

User = get_user_model()
"""
Just a temp solution for holiday exception.
"""

days = Day.objects.all()
HOLIDAYS = [day.date for day in days if day.is_holiday]
EXTRA_WORKDAY = [day.date for day in days if not day.is_holiday]
THRESHOLD_LIST = [3, 7, 30]


def is_weekday(date):
    """
    Check if a Python's datetime.date or datetime.datetime is a weekday.
    """
    return (date.isoweekday() <= 5)


def date_range(start, end):
    """
    Given two datetime.date or datetime.datetime, retrun a date range.
    """
    days = (end - start).days
    date_range = [start + timedelta(n) for n in range(days)]
    return date_range


class Command(BaseCommand):
    help = 'Commands of notifying users of the diary app.'

    def handle(self, *args, **options):
        """
        Create a checklist.
        """
        users = User.objects.filter(profile__keep_diary=True)
        wanted = {}
        for user in users:
            start = user.profile.diary_starting_date
            end = today()
            past_dates = date_range(start, end)
            past_weekday_dates = [date for date in past_dates if is_weekday(date) and date not in HOLIDAYS]
            past_work_dates = past_weekday_dates + EXTRA_WORKDAY
            past_work_dates = sorted(past_work_dates)
            for date in past_work_dates:
                wanted.update({(date, user.id): False})
        """
        Create a dictionary using a tuple ``date`` and ``created_by_id`` as key,
        Because we only need these two fields to check if there is lack of diary.
        Note that in Django Sunday = 1, in python datetime Sunday = 6.
        """
        diarys = Diary.objects.filter(date__week_day__gte=2).filter(date__week_day__lte=7)  # Monday to Friday
        values_list = diarys.values_list('date', 'created_by_id')
        existed = {(values): True for values in values_list}
        """
        Compare them.
        """
        wanted.update(existed)
        """
        Formatting
        """
        results = [(key[1], key[0]) for key, value in wanted.items() if value is False]
        results_dict = {}
        for user_id, date in results:
            if user_id not in results_dict:
                results_dict[user_id] = []
            results_dict[user_id].append(date)
        """
        Sending Emails.
        """
        for user_id, dates in results_dict.items():
            user = User.objects.get(id=user_id)
            username = user.username
            email = user.email
            datestrings = [str(date) for date in dates]
            subject = f'[TDB]工程師日誌-{username}，您有 {len(dates)} 筆日誌還沒有紀錄。'
            message = f'Hi {username},\n\n您有 {len(dates)} 筆工程師日誌還沒有紀錄，以下為日期：\n\n' + '\n'.join(datestrings) + '\n\nSincerely,\nTDB'
            recipient_list = [email]
            notification_level = 1
            oldest_date = sorted(dates)[0]
            late_days = (today() - oldest_date).days
            for threshlod in THRESHOLD_LIST:
                if late_days >= threshlod:
                    notification_level += 1
                else:
                    break
            person_notified = user
            while notification_level >= 1 and person_notified:
                notification_level -= 1
                if person_notified.email not in recipient_list:
                    recipient_list.append(person_notified.email)
                person_notified = person_notified.profile.boss
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=recipient_list,
                fail_silently=False,
            )
            print(f'An Email for user {username} has been sent to {recipient_list}, dates={datestrings}')
