from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Commands of notifying users of the diary app.'

    def handle(self, *args, **options):
        """
        To be implemented.
        """
        print('Handling notifying users of the diary app.')
        print('..')
        print('..')
        print('Finished!')
