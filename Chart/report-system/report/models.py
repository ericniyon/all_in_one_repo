from django.db import models
from timezone_field import TimeZoneField
import arrow
import datetime
from django.core.mail import send_mail
from django.contrib import messages
from django.core.exceptions import ValidationError

class Report(models.Model):
    creator = models.ForeignKey("human_security.User", null=True,  on_delete=models.CASCADE)
    sector = models.ForeignKey("human_security.Sector",  on_delete=models.CASCADE)
    kpi = models.ForeignKey("human_security.KPI",  on_delete=models.CASCADE)
    from_to_date = models.DateField( auto_now=False, auto_now_add=False)
    up_to_date=models.DateField( auto_now=False, auto_now_add=False)
    notes = models.TextField()
    reported_on = models.DateTimeField(auto_now_add=True, null=True)
    time_zone = TimeZoneField(default='UTC')


    def clean(self):
    
        report_time = arrow.get(self.from_to_date, self.time_zone)
        if report_time > arrow.utcnow():
            raise ValidationError(

                'You cannot schedule a report for the future. '
                'Please check your time to continue'
        )


    def __str__(self):
        return str(self.id)


    def send_mail(self):

        weekday = 4

        days_ahead = weekday - self.reported_on.weekday()
        if days_ahead <= 0:
            days_ahead += 7

        next_friday = self.reported_on + datetime.timedelta(days_ahead)
        if self.time_zone == next_friday :
            send_mail(
                'report remainder', 
                'Hey! you have not send report for last week please submitt your report inorder to help others to kwnow what is going on', 
                'niyoeri6@gmail.com',
                ['niyoeri6@gmail.com'],
                fail_silently=False
                )

            return redirect('/')


        





