from django.shortcuts import render
from django.core.mail import send_mail
from EmailConfirmationP.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from .models import ReportType

def returning_same(request):

    subject = "Welcome "
    message = 'We are in Reporting period you need to submitt your report on time !!!'
    
    recepient = 'niyoeri6@gmail.com'
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return HttpResponse('Email been sent successfully !!!!!!!!!')
            
        