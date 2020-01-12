from django.contrib import admin
from .models import Report,TypesOfReport
# Register your models here.
class ReportAdminb(admin.ModelAdmin):
        list_display = ('report_type','igihe_itangirwa','deadline','owner')

class ReportAdmin(admin.ModelAdmin):
        list_display = ('report_name','report_file','submitted_on',)

admin.site.register(Report, ReportAdmin)

admin.site.register(TypesOfReport,ReportAdminb)
