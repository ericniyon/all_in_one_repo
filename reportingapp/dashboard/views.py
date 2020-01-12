from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Result, Sector, KPI
from django.db.models import Sum, Count


class DashboardView(ListView):
    model = Result
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['kpis'] = KPI.objects.all()
        context['results'] = Result.objects.filter(sector=self.request.user.user_profile.sector)
        context['achieved_results'] = Result.objects.filter(achieved=0, sector=self.request.user.user_profile.sector)
        context['pending_results'] = Result.objects.filter(pending=0, sector=self.request.user.user_profile.sector)
        context['sectors'] = Sector.objects.all()
        # context['results_by_kpi'] = Result.objects.all().filter(kpi_id=self.kwargs['kpi_id'])
        context['achieved_total'] = Result.objects.values('kpi__name', 'kpi_id').annotate(achieved=Sum('achieved')).annotate(pending=Sum('pending'))


        context['seed_sector'] = Result.objects.values('kpi__name', 'kpi_id').annotate(achieved=Sum('achieved')).annotate(pending=Sum('pending')).filter(sector=self.request.user.user_profile.sector)


        return context


class KPIDetailView(DetailView):
    model = KPI
    template_name = "dashboard/kpi_detail.html"

    def get_context_data(self, **kwargs):
        context = super(KPIDetailView, self).get_context_data(**kwargs)
        context['performance_kpi_sectors'] = Result.objects.filter(kpi_id=self.kwargs['pk'])
        context['kpis'] = KPI.objects.all()
        context['current_kpi'] = Result.objects.filter(kpi_id=self.kwargs['pk']).values_list('kpi__name').distinct()
        return context

