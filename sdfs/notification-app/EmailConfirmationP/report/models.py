from django.db import models
from django.contrib.auth.models import User
from mainApp.models import *
import datetime
from time import gmtime, strftime
from datetime import timedelta, date
from EmailConfirmationP.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models.signals import post_save

class UserProfile(models.Model):
    SECTOR = 1
    DISTRICT = 2
    SUPER = 3
    ROLE_CHOICES = (
        (SECTOR, 'Sector Level User'),
        (DISTRICT, 'District Level User'),
        (SUPER, 'Super Level User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='sector_profiles')
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=1)

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    def __str__(self):
        return self.user.get_username()


def geting_date():
    initial_date = datetime.date(2019,12,1)
    deadline = initial_date + datetime.timedelta(days=23,hours=14, minutes=44)
    return deadline


class ReportType(models.Model):

    ICYUMWERU = 1
    IGIHEMBWE = 2
    UMWAKA = 3
    TIME_CHOICES = (
        (ICYUMWERU, 'Icyumweru'),
        (IGIHEMBWE, 'Igihembwe'),
        (UMWAKA, 'Umwaka'),
    )

    r_type = models.CharField(max_length=300)
    igihe_itangirwa = models.PositiveSmallIntegerField(choices=TIME_CHOICES, default=1)
    owner = models.ForeignKey(User, models.CASCADE)
    department = models.ForeignKey(Department, models.CASCADE)
    deadline = models.DateField(default=geting_date)


    def mail_remainder(self):

        week = self.deadline - datetime.timedelta(days=30)

        report_remainder = self.deadline - datetime.timedelta(days=5)
        final_email = self.deadline

        if week== True and self.igihe_itangirwa == 'Icyumweru':
            subject = "Welcome "
            message = 'We are in Reporting period you need to submitt your report on time !!!'
            rec = self.owner.email
            recepient = rec
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)


            
        elif report_remainder==True and self.igihe_itangirwa == 'Igihembwe':
            subject = "Welcome "
            message = 'We are in Reporting period you need to submitt your report on time !!!'
            rec = self.owner.email
            recepient = rec
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)

        elif final_email==True and self.igihe_itangirwa=='Umwaka':
            subject = "Welcome "
            message = 'We are in Reporting period you need to submitt your report on time !!!'
            rec = self.owner.email
            recepient = rec
            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)


        
            
        

            
    def __str__(self):
        return self.r_type

    



class Report(models.Model):
    report_type = models.ForeignKey(ReportType, models.CASCADE)
    doc = models.FileField()


