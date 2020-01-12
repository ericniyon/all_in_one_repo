from django.db import models
from core.models import UserProfile
from dashboard.models import Department
import datetime
from django.utils import timezone
from datetime import timedelta, date
from district_reporting.settings import EMAIL_HOST_USER
from django.core.mail import send_mail




def get_deadline():
    # initial_date = datetime.datetime(2019, 12, 1, 2, 25, 10, 291224)
    initial_date = datetime.datetime.utcnow()

    deadlines = initial_date + datetime.timedelta(minutes=5)
    return deadlines

class ReportType(models.Model):
    WEEK = 1
    TERM = 2
    YEAR = 3
    TIME_CHOICES = (
        (WEEK, 'Icyumweru'),
        (TERM, 'Igihembwe'),
        (YEAR, 'Umwaka'),
    )
    report_type = models.CharField(max_length=300)
    igihe_itangirwa = models.PositiveSmallIntegerField(choices=TIME_CHOICES)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    deadline = models.DateTimeField(default=get_deadline)


  
  

    def __str__(self):
        return self.report_type


class Report(models.Model):
    report_type     = models.ForeignKey(ReportType, on_delete=models.CASCADE)
    report_file     = models.FileField(upload_to='reports')
    submited_date   = models.DateTimeField(auto_now_add=True)



def mail( *args, **kwargs):
    subject = "Welcome "
    message = 'New Report has been added successfully !!!'
    recepient = 'niyoeri6@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient])

    return None
