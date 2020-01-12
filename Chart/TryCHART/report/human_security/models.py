from django.contrib.auth.models import AbstractUser
from django.db import models


class District(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"

    def __str__(self):
        return self.name


###### added by Taufique#########################
class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

############################################################

class KPI(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "KPI"
        verbose_name_plural = "KPIs"

    def __str__(self):
        return self.name


class Result(models.Model):
    achieved = models.IntegerField()
    pending = models.IntegerField()
    name = models.CharField(max_length=30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    # kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, related_name='kpi_results')
    # sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='sector_results')
    # date_added = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"

    def __str__(self):
        return str(self.id)


################################################################################

class User(AbstractUser):
    is_reporter = models.BooleanField('reporter status', default=False)
    # is_active = models.BooleanField(default=True)
    # date_joined = models.DateTimeField(default=timezone.now)
    # sector = models.ForeignKey(Sector, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.username


class Reporter(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.ManyToManyField(Location)