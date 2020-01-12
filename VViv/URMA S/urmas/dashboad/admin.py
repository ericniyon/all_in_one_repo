from django.contrib import admin
from .models import TransportMean, Report, Staff, Category, Department, Mission, Role, SchoolModel


class StaffDesplays(admin.ModelAdmin):
    list_display=('name','category','department','role')
    list_filter=('role',)
    search_fields=['category', 'role']

class MissionsDesplays(admin.ModelAdmin):
    list_display=('purpose','result','destnation','distance','dipature_date','returnning_date','duration_of_mission')
    list_filter=('dipature_date',)
    search_fields=['purpose']

class ReportDesplays(admin.ModelAdmin):
    list_display=('file','note',)



admin.site.register(TransportMean)
# admin.site.register(Requeste)
admin.site.register(Staff,StaffDesplays)
admin.site.register(Department)
admin.site.register(Mission,MissionsDesplays)
admin.site.register(Role)
admin.site.register(Category)
admin.site.register(Report)
admin.site.register(SchoolModel)



