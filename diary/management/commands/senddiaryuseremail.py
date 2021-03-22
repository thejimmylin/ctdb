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

    def get_diary_users(self):
        """
        Get all user who need to write diary.
        """
        return User.objects.filter(profile__keep_diary=True)

    def get_diary_needed(self, users):
        """
        Generate a dict with (`user.id`, `date`) as key and boolean value as value.
        This is for recording what kind of diary we need.
        """
        wanted = {}
        for user in users:
            start = user.profile.diary_starting_date
            end = today()
            dates = date_range(start, end)
            weekday_dates = [date for date in dates if is_weekday(date)]
            workday_dates = [date for date in weekday_dates if date not in HOLIDAYS]
            wanted_dates = set(workday_dates) | set(EXTRA_WORKDAY)
            sorted_wanted_dates = sorted(list(wanted_dates))
            for date in sorted_wanted_dates:
                wanted.update({(user.id, date): False})
        return wanted

    def get_diary_existing(self):
        """
        Generate a dictionary with (`created_by_id`, `date`) as key and boolean value as value.
        This is to recording what kind of diary we have.
        """
        diaries = Diary.objects.all()
        diary_values_list = diaries.values_list('created_by_id', 'date')
        existing = {(values): True for values in diary_values_list}
        return existing

    def get_diary_missing(self, needed, existing):
        """
        Generate a dictionary with `user.id` as key and a list of `date` as value.
        This is to recording what kind of diary we are missing.
        """
        needed.update(existing)
        missing = {}
        for key, value in needed.items():
            if value:
                continue
            user_id, date = key
            if user_id not in missing:
                missing[user_id] = []
            missing[user_id].append(date)
        return missing

    def send_email(self, missing):
        for user_id, dates in missing.items():
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
            # send_mail(
            #     subject=subject,
            #     message=message,
            #     from_email=settings.DEFAULT_FROM_EMAIL,
            #     recipient_list=recipient_list,
            #     fail_silently=False,
            # )
            print(f'An Email for user {username} has been sent to {recipient_list}, dates={datestrings}')

    def handle(self, *args, **options):
        users = self.get_diary_users()
        needed = self.get_diary_needed(users=users)
        existing = self.get_diary_existing()
        missing = self.get_diary_missing(needed=needed, existing=existing)
        self.send_email(missing=missing)