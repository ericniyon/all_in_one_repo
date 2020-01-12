from django.urls import path, include
from .views import DashboardView, KPIDetailView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('kpi/<int:pk>', KPIDetailView.as_view(), name='kpi-detail')
]