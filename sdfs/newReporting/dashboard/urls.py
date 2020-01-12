from django.urls import path, include
from .views import DashboardView, KPIDetailView, Ibyakozwe

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('kpi/<int:pk>', KPIDetailView.as_view(), name='kpi-detail'),
    path('ibyakozwe/<int:pk>', Ibyakozwe.as_view(), name='ibyakozwe'),
    path('ibisigaye/<int:pk>', Ibyakozwe.as_view(), name='ibisigaye'),
    path('ibyakozwe_sector/<int:pk>', Ibyakozwe.as_view(), name='ibyakozwe_sector'),
    path('ibisigaye_sector/<int:pk>', Ibyakozwe.as_view(), name='ibisigaye_sector'),
]