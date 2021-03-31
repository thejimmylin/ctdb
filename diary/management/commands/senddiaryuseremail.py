import logging

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.template import loader

from core.mail import send_mail
from core.utils import date_range, today
from day.models import Day
from diary.models import Diary

# Get an instance of a logger
logger = logging.getLogger(__name__)


User = get_user_model()


class Command(BaseCommand):
    help = 'Commands of notifying users of the diary app.'

    HOLIDAYS = [day.date for day in Day.objects.all() if day.is_holiday]
    EXTRA_WORKDAY = [day.date for day in Day.objects.all() if not day.is_holiday]
    THRESHOLD_LIST = [3, 7, 30]
    SUBJECT_TEMPLATE_NAME = 'diary/mails/diary_missing_notification_subject.txt'
    BODY_TEMPLATE_NAME = 'diary/mails/diary_missing_notification_body.html'

    def add_arguments(self, parser):
        parser.add_argument(
            '--debug',
            action='store_true',
            default=settings.DEBUG,
            help=(
                'If set to `False`, the command would still log the messages but the Email would not be sent.'
                'Defalut to `settings.DEBUG`'
            ),
        )

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
        needed = {}
        for user in users:
            start_date = user.profile.diary_starting_date
            end_date = today()
            dates = date_range(start_date, end_date)
            weekday_dates = [date for date in dates if date.isoweekday() <= 5]
            workday_dates = [date for date in weekday_dates if date not in self.HOLIDAYS]
            needed_dates = set(workday_dates) | set(self.EXTRA_WORKDAY)
            sorted_needed_dates = sorted(list(needed_dates))
            for date in sorted_needed_dates:
                needed.update({(user.id, date): False})
        return needed

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

    def get_notification_level(self, past_days):
        """
        Given a `past_days`, return a `notification_level`.
        If `notification_level` == 1, the user's boss will be added into `CC`.
        If `notification_level` == 2, the user's boss, and the boss' boss will be added into `CC`.
        """
        notification_level = 0
        for threshold in self.THRESHOLD_LIST:
            if past_days >= threshold:
                notification_level += 1
            else:
                break
        return notification_level

    def get_cc(self, user, notification_level):
        """
        Given a `user` and a `notification_level`,
        return a CC, which is nothing more than a list of Email string.
        """
        cc = []
        while notification_level > 0:
            supervised_by_roles = []
            roles = user.groups.filter(groupprofile__is_role=True)
            for role in roles:
                _supervised_by_roles = role.group.supervised_by_roles.all()
                if _supervised_by_roles:
                    for role in _supervised_by_roles:
                        if role not in supervised_by_roles:
                            supervised_by_roles.append(role)
            users = []
            for role in supervised_by_roles:
                users.append(role.group.user_set.all())
            for user in users:
                cc.append(user.email)
            notification_level = notification_level - 1
        return cc

    def get_email_configs(self, missing, test=True):
        """
        Given a dictionary with `user.id` as key and a list of `date` as value, It
        would generate a Email config list like this:
        [
            {'subject': subject1, 'body': body1, 'to': to1, 'cc', cc1},
            {'subject': subject2, 'body': body2, 'to': to2, 'cc', cc2},
            ...
        ]
        """
        email_configs = []
        for user_id, dates in missing.items():
            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                continue
            username = user.username
            datestrings = ', '.join(str(date) for date in dates)
            context = {'username': username, 'dates': dates, 'datestrings': datestrings}
            subject = loader.render_to_string(self.SUBJECT_TEMPLATE_NAME, context)
            body = loader.render_to_string(self.BODY_TEMPLATE_NAME, context)
            to = [user.email]
            notification_level = self.get_notification_level(past_days=(today() - min(dates)).days)
            cc = self.get_cc(user=user, notification_level=notification_level)

            email_config = {
                'subject': subject,
                'body': body,
                'to': to,
                'cc': cc,
            }
            email_configs.append(email_config)
        return email_configs

    def handle(self, *args, **options):
        users = self.get_diary_users()
        diary_needed = self.get_diary_needed(users=users)
        diary_existing = self.get_diary_existing()
        diary_missing = self.get_diary_missing(needed=diary_needed, existing=diary_existing)
        email_configs = self.get_email_configs(missing=diary_missing)
        for config in email_configs:
            subject, body, to, cc = config['subject'], config['body'], config['to'], config['cc']
            if not options['debug']:
                send_mail(subject=subject, body=body, to=to, cc=cc)
            log = (
                f'to:\n{to}\n'
                f'cc:\n{cc}\n'
                f'subject:\n{subject}\n'
                f'body:\n{body}'
            )
            logger.info(log)
