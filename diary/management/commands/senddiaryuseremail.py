from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.core.management.base import BaseCommand
from django.utils import timezone

from diary.models import Diary


START_YEAR = 2021
START_MONTH = 1
START_DAY = 1
SUPERVISOR_GROUP_NAME = 'Supervisors'
WRITING_DIARY_DEPS = ['T32', ]

User = get_user_model()


def startday(year=START_YEAR, month=START_MONTH, day=START_DAY):
    return datetime(year=year, month=month, day=day).date()


def is_diarist(user):
    if user.groups.filter(name=SUPERVISOR_GROUP_NAME).exists():
        return False
    return user.profile.department.filter(name__in=WRITING_DIARY_DEPS).exists()


def get_supervisors(user):
    user_deps = user.profile.department.all()
    all_supervisors = User.objects.filter(groups__name__in=[SUPERVISOR_GROUP_NAME])
    user_supervisors = all_supervisors.filter(profile__department__in=user_deps)
    return user_supervisors


def today():
    return timezone.localtime(timezone.now()).date()


class Command(BaseCommand):
    help = 'Commands of notifying users of the diary app.'

    def handle(self, *args, **options):
        """
        Create a checklist.
        """
        day_passed = (today() - startday()).days
        past_dates = [startday() + timedelta(n) for n in range(day_passed)]
        past_weekday_dates = [date for date in past_dates if date.weekday() <= 4]
        user_ids = [user.id for user in User.objects.all()]
        wanted = {
            (date, created_by_id): False
            for created_by_id in user_ids
            for date in past_weekday_dates
        }
        """
        Create a dictionary using a tuple ``date`` and ``created_by_id`` as key,
        Because we only need these two fields to check if there is lack of diary.
        Note that in Django Sunday = 1, in python datetime Sunday = 6.
        """
        diarys = Diary.objects.filter(date__week_day__gte=2).filter(date__week_day__lte=7)  # weekday
        values = diarys.values()
        existed = {
            (value['date'], value['created_by_id']): True for value in values
        }
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
            """
            Diarists filter. (If you are a diarist, you have to write diary every day.)
            """
            if is_diarist(user):
                username = user.username
                email = user.email
                datestrings = [str(date) for date in dates]
                subject = f'[TDB]工程師日誌-您有 {len(dates)} 筆日誌還沒有紀錄'
                message = f'Hi {username},\n\n您有 {len(dates)} 筆工程師日誌還沒有紀錄，以下為日期：\n\n' + '\n'.join(datestrings) + '\n\nSincerely,\nTDB'
                recipient_list = [email]
                has_to_notify_supervisor = False
                for date in dates:
                    if (today() - date).days >= 3:
                        has_to_notify_supervisor = True
                if has_to_notify_supervisor:
                    supervisors = get_supervisors(user)
                    for supervisor in supervisors:
                        if supervisor.email not in recipient_list:
                            recipient_list.append(supervisor.email)
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=recipient_list,
                    fail_silently=False,
                )
                print(f'An Email about {username} has been sent to {recipient_list}.')
