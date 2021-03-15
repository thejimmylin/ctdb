from django.core.management.base import BaseCommand
from reminder.models import Reminder
from core.utils import today
from django.core.mail import send_mail


class Command(BaseCommand):
    help = 'Commands of send reminder Email.'

    def handle(self, *args, **options):
        reminders = Reminder.objects.filter(is_active=True, start_date__lte=today(), stop_date__gt=today())
        for reminder in reminders:
            reminder.policy, reminder.advanced_policy
            if reminder.policy == 'on weekdays':
                pass
            elif reminder.policy == 'daily':
                pass
            elif reminder.policy == 'advanced policy':
                pass
            else:
                pass
