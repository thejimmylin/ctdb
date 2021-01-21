from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from diary.models import Diary


class Command(BaseCommand):
    help = 'Commands of notifying users of the diary app.'

    def handle(self, *args, **options):
        User = get_user_model()
        users = User.objects.all()
        for user in users:
            print(f'username = "{user.username}", email = "{user.email}"')
            diarys = Diary.objects.filter(created_by=user)
            for diary in diarys:
                print('Diarys:\n')
                print(f'id = {diary.id}, daily_record = "{diary.daily_record}"')
                """
                Send Email..
                """
                # subject = 'foo'
                # message = 'bar'
                # send_mail(
                #     subject=subject,
                #     message=message,
                #     from_email=settings.DEFAULT_FROM_EMAIL,
                #     recipient_list=['b00502013@gmail.com'],
                #     fail_silently=False,
                # )
