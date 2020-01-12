from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class District(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "District"
        verbose_name_plural = "Districts"

    def __str__(self):
        return self.name


class Sector(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='district_sectors')

    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectors"

    def __str__(self):
        return self.name


class KPI(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "KPI"
        verbose_name_plural = "KPIs"

    def __str__(self):
        return self.name


class Result(models.Model):
    achieved = models.PositiveIntegerField()
    pending = models.PositiveIntegerField()
    kpi = models.ForeignKey(KPI, on_delete=models.CASCADE, related_name='kpi_results')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, related_name='sector_results')
    date_added = models.DateTimeField(auto_now=True)
    year = models.PositiveIntegerField(default=current_year())

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        unique_together = ("sector", "kpi", "year")

    def __str__(self):
        return str(self.kpi)



