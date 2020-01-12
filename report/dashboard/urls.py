from django.urls import path, include
from .views import DashboardView, get_data, PieChartData

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('api/data/', get_data, name='api-data'),
    path('api/chart/data/', PieChartData.as_view())

]