from datetime import datetime

from apscheduler.schedulers.background import BackgroundScheduler
from .models import * 


import datetime
# from datetime import timezone


def trimester_from_now():
     term = datetime.date.today() + datetime.timedelta((3*365/12) + 3)
     return term


def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + datetime.timedelta(days_ahead)

d = datetime.datetime(2019,12,28)
next_friday = next_weekday(d, 4)
print('Next++',next_friday)




def start(deadline):
    # today = datetime.datetime.today()
    reports =  ReportType.objects.all()

    for simple in reports:
        if simple.igihe_itangirwa ==1:

            deadlina = next_weekday(d,4)
            scheduler = BackgroundScheduler()
            scheduler.add_job(mail, 'date', run_date=deadlina)
            scheduler.start()

        elif simple.igihe_itangirwa ==2:
            from calendar import monthrange

            days_in_month = lambda dt: monthrange(dt.year, dt.month)[1]
            today = date.today()
            therd_day = today.replace(day=3) + timedelta(days_in_month(today))

            deadlina = simple.deadline + datetime.timedelta(days=20)
            scheduler = BackgroundScheduler()
            scheduler.add_job(mail, 'date', run_date=therd_day)
            scheduler.start()

         elif simple.igihe_itangirwa ==3:
            

            deadlina = trimester_from_now
            scheduler = BackgroundScheduler()
            scheduler.add_job(mail, 'date', run_date=deadlina)
            scheduler.start()

