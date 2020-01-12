
from django.urls import path, include

from report.views import (
    CreateReport ,
    ListAllReports,
    ReportDetails,
    Export_to_CSV,
 
        )

urlpatterns = [

    path('', CreateReport, name='new_report'),
    path('list/', ListAllReports, name='report_list'),
    path('details/<int:pk>', ReportDetails, name='report_details'),
    path('export/csv/', Export_to_CSV, name='export_to_csv'),


]
