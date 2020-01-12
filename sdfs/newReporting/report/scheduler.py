import datetime
from datetime import date
from apscheduler.schedulers.background import BackgroundScheduler
from .models import *

    

def schedule_reminder():
    # report = ReportType.objects.values('id')
    # print(report)

    schedule_reminder=datetime.datetime.now() + datetime.timedelta(days=5)
    if schedule_reminder:
        scheduler = BackgroundScheduler()
        scheduler.add_job(mail, 'date', run_date=date(schedule_reminder))
        scheduler.start()
    
    return schedule_reminder
    
