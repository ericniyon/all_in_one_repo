from django.urls import path, include
from .views import generate_report

urlpatterns = [
    path('', generate_report, name='reporting'),
]