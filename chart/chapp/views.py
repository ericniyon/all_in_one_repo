from django.shortcuts import render
from .models import CartData
from django.db.models import Count, Q



def chart_class_view(request):
    dataset = CartData.objects \
        .values('groupe') \
        .annotate(survived_count=Count('groupe', filter=Q(survived=True)),
                  not_survived_count=Count('groupe', filter=Q(survived=False)),
                  climate_hot=Count('climate', filter=Q(climate='hot')),
                  climate_cold=Count('climate', filter=Q(climate='cold'))) \
        .order_by('groupe')
    return render(request, 'chart_one.html', {'dataset': dataset})

