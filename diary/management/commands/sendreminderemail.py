from django.core.management.base import BaseCommand
from reminder.models import Reminder
from core.utils import today


class Command(BaseCommand):
    help = 'Commands of send reminder Email.'

    def handle(self, *args, **options):
        reminders = Reminder.objects.filter(is_active=True, start_date__lte=today(), stop_date__gt=today())
        for reminder in reminders:
            period = reminder.period
            print(period)
