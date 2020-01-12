from django.urls import path, include
from .views import AgricultureListView

urlpatterns = [
    path('crops', AgricultureListView.as_view(), name='crops'),
    path('seeds', AgricultureListView.as_view(), name='seeds'),
    path('ubwanikiro', AgricultureListView.as_view(), name='ubwanikiro'),
    path('terassis', AgricultureListView.as_view(), name='terassis'),
    path('banana', AgricultureListView.as_view(), name='banana'),
    path('fertilizer', AgricultureListView.as_view(), name='fertilizer'),
    path('training', AgricultureListView.as_view(), name='trainings'),
    path('vaccination', AgricultureListView.as_view(), name='vaccinations'),
    path('insemination', AgricultureListView.as_view(), name='insemination'),
    path('inkazizakurikiranwa', AgricultureListView.as_view(), name='inkazizakurikiranwa'),
    path('girinka', AgricultureListView.as_view(), name='girinka'),
    path('umuhigo', AgricultureListView.as_view(), name='imihigo'),
    path('irrigation', AgricultureListView.as_view(), name='irrigation'),
    path('pumps_number', AgricultureListView.as_view(), name='pumps'),
    path('improved_seeds', AgricultureListView.as_view(), name='improved_seeds'),

    path('sector-crop', AgricultureListView.as_view(), name='crop_sector'),
    path('sector-seed', AgricultureListView.as_view(), name='seed_sector'),
    path('sector-ubwanikiro', AgricultureListView.as_view(), name='ubwanikiro_sector'),
    path('sector-terassis', AgricultureListView.as_view(), name='terrassis_sector'),
    path('sector-banana', AgricultureListView.as_view(), name='banana_sector'),
    path('improved_seeds_sector', AgricultureListView.as_view(), name='improved_seed_sector'),
    path('insemination_sector', AgricultureListView.as_view(), name='insemination_sector'),
    path('inkazizakurikiranwa_sector', AgricultureListView.as_view(), name='inkazizakurikiranwa_sector'),
    path('girinka_sector', AgricultureListView.as_view(), name='girinka_sector'),
    path('training_sector', AgricultureListView.as_view(), name='training_sector'),

    path('fertilizer_sector', AgricultureListView.as_view(), name='fertilizer_sector'),
    path('vaccination_sector', AgricultureListView.as_view(), name='vaccination_sector'),
    path('irrigated_sector', AgricultureListView.as_view(), name='irrigated_sector'),
    path('number_of_pump_sector', AgricultureListView.as_view(), name='number_of_pump_sector'),
    path('imihigo_sector', AgricultureListView.as_view(), name='imihigo_sector'),
]