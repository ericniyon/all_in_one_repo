from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView, CreateView


from human_security.models import Sector, District, KPI, Result

from rest_framework.views import APIView
from rest_framework.response import Response

from human_security.models import User


class DashboardView(ListView):
    model = Result
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        # context['kpis'] = KPI.objects.all()
        # context['sectors'] = Sector.objects.all()
        # context['results'] = Result.objects.filter(sector=self.request.user.sector)
        # context['achieved_results'] = Result.objects.filter(achieved=0, sector=self.request.user.sector)
        # context['pending_results'] = Result.objects.filter(pending=0, sector=self.request.user.sector)
        return context



class PieChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        achieved = list(Result.objects.all().filter(sector__name__contains='Kigabiro').values('achieved'))
        pending = list(Result.objects.all().filter(sector__name__contains='Kigabiro').values('pending'))
        labels = ["Achieved", 'Pending']
        default_items = [achieved, pending]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)


def get_data(request):
    achieved = list(Result.objects.values('achieved'))
    pending = list(Result.objects.values('pending'))
    labels = ['Achieved', 'Pending']
    default_items = [achieved, pending]
    data = {
        "labels": labels,
        "default": default_items,
    }
    return JsonResponse(data)





