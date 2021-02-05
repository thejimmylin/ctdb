from datetime import date as datetime_date, timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.utils import timezone

from diary.models import Diary


User = get_user_model()
"""
Just a temp solution for holiday exception.
"""

NEW_YEAR_HOLIDAYS = [
    datetime_date(2021, 2, 10) + timedelta(n) for n in range(7)
]
THRESHOLD_LIST = [3, 7, 30]


def today():
    return timezone.localtime(timezone.now()).date()


def is_weekday(date):
    return (date.weekday() <= 4)


class Command(BaseCommand):
    help = 'Commands of notifying users of the diary app.'

    def handle(self, *args, **options):
        """
        Create a checklist.
        """
        users = User.objects.filter(profile__keep_diary=True)
        wanted = {}
        for user in users:
            starting_date = user.profile.diary_starting_date
            past_date_list = [starting_date + timedelta(n) for n in range((today() - starting_date).days)]
            past_weekday_date_list = [date for date in past_date_list if is_weekday(date) and date not in NEW_YEAR_HOLIDAYS]  # Temp solution
            for date in past_weekday_date_list:
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
