from django.apps import AppConfig


class ReportConfig(AppConfig):
    name = 'report'

    def ready(self):
        from report import scheduler
        scheduler.schedule_reminder()
