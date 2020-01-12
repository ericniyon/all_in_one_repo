from django.shortcuts import render,get_object_or_404
from human_security.models import User, KPI, Sector
from .models import Report
from django.contrib import messages
from .forms import ReportCreationForm
from django.core.mail import send_mail
import csv
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import EmailMessage


# Welcome mail with follow up example
from datetime import timedelta
from django.utils import timezone
from django_q.tasks import async_task, schedule
from django_q.models import Schedule


def welcome_mail(user):
    msg = 'Welcome to our website'
    # send this message right away
    async_task('django.core.mail.send_mail',
            'Welcome',
            msg,
            'niyoeri6@gmail.com',
            [user.email])
    # and this follow up email in one hour
    msg = 'Here are some tips to get you started...'
    schedule('django.core.mail.send_mail',
             'Follow up',
             msg,
             'from@example.com',
             [user.email],
             schedule_type=Schedule.ONCE,
             next_run=timezone.now() + timedelta(hours=1))

    # since the `repeats` defaults to -1
    # this schedule will erase itself after having run
def CreateReport(request):
    template_name =  "report/create.html"
    form = ReportCreationForm(request.POST or None)

    if form.is_valid():
        form.save()

        report_creator=form.save()
        report_creator.creator = request.user
        report_creator.save()

        messages.success(request,'Report has been created successfully !!!!')
        form = ReportCreationForm()

 
    context={
        'form':form,
    }

    return render(request, template_name, context)


def ListAllReports(request):
    template_name = "report/create.html"
    reports = Report.objects.filter(creator=request.user)

    context={
        'reports':reports
    }

    return render(request, template_name, context)



def ReportDetails(request, pk):
    template_name = "report/create.html"
    data = get_object_or_404(Report, pk=pk)

    context = {
        'data':data
    }

    return render(request, template_name, context)
    
    

def Export_to_CSV(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reports.csv"'
    writer = csv.writer(response)
    writer.writerow(['creator','sector','kpi','from_to_date','up_to_date','notes'])

    reports= Report.objects.all().values_list('creator','sector','kpi','from_to_date','up_to_date')

    for report in reports:
        writer.writerow(report)

    return response