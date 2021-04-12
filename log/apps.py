from django.apps import AppConfig


class LogConfig(AppConfig):
    name = 'log'

    def ready(self):
        import log.signals  # noqa
