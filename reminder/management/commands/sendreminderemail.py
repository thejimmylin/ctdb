from django.core.management.base import BaseCommand
from reminder.models import Reminder
from core.utils import today
from django.core.mail import send_mail
from django.conf import settings


class Command(BaseCommand):
    help = 'Commands of send reminder Email.'
    WEEK_MAP = {
        0: 'monday',
        1: 'tuesday',
        2: 'wednesday',
        3: 'thursday',
        4: 'friday',
        5: 'saturday',
        6: 'sunday',
    }

    def handle(self, *args, **options):
        # Daily
        qs = Reminder.objects.filter(is_active=True, policy='daily', start_at__lte=today(), end_at__gt=today())
        for reminder in qs:
            self.handle_mail(reminder)
        # On weekdays
        qs = Reminder.objects.filter(is_active=True, policy='on weekdays', start_at__lte=today(), end_at__gt=today())
        for reminder in qs:
            self.handle_mail(reminder)
        # Once
        qs = Reminder.objects.filter(is_active=True, policy='once', start_at__lte=today())
        for reminder in qs:
            self.handle_mail(reminder)
        # Every Monday, every tuesday, every Wednesday, every Thursday, every Friday, every Saturday, every Friday
        code = today().weekday()
        suffix = self.WEEK_MAP[code]
        policy = 'every ' + suffix
        qs = Reminder.objects.filter(is_active=True, policy=policy, start_at__lte=today(), end_at__gt=today())
        for reminder in qs:
            self.handle_mail(reminder)
        # Specified dates
        qs = Reminder.objects.filter(is_active=True, policy='specified dates')
        for reminder in qs:
            dates = reminder.specified_dates
            seperator = ','
            dates = dates[:-1] if dates[-1:] == seperator else dates
            date_list = list(map(str.strip, dates.split(';')))
            if str(today()) in date_list:
                self.handle_mail(reminder)

    def handle_mail(self, reminder, debug=True):
        seperator = ';'
        recipients = reminder.recipients[:-1] if reminder.recipients[-1:] == seperator else reminder.recipients
        recipient_list = list(map(str.strip, recipients.split(';')))
        if debug:
            print("Sending a Email to ", recipient_list)
            print("Email:\n")
            print(reminder.email_subject)
            print(reminder.email_content)
        send_mail(
            subject=reminder.email_subject,
            message=reminder.email_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
            fail_silently=False,
        )
