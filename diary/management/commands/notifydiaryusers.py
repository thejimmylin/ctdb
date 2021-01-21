from django.core.management.base import BaseCommand
from django.conf import settings
from django.core.mail import send_mail
from diary.models import Diary


class Command(BaseCommand):
    help = 'Commands of notifying users of the diary app.'

    def handle(self, *args, **options):
        """
        To be implemented.
        """
        print('Handling notifying users of the diary app.')
        print(Diary.objects.all())
        subject = 'Hello world.'
        message = 'hello, how are you?'
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['b00502013@gmail.com'],
            fail_silently=False,
        )
        print('..')
        print('..')
        print('Finished!')
