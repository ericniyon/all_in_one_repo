from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import District, Sector, KPI, Result, User, Location, Reporter

admin.site.register(District)
admin.site.register(Sector)
admin.site.register(KPI)
admin.site.register(Result)
admin.site.register(User)
admin.site.register(Reporter)
admin.site.register(Location)



