from django.apps import AppConfig


class ReportappConfig(AppConfig):
    name = 'reportapp'

    def ready(deadline):
        from reportapp import scheduler
        scheduler.start(deadline)
