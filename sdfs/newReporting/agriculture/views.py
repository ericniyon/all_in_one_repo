from django.shortcuts import render
from django.views.generic import ListView

from agriculture.models import (Crops, Seeds, Ubwanikiro, UnusedTerassis, Umuhigo, Pumps_in_Sector,
                                Banana_and_Rehabilitation, InkaZizakurikiranwa, Girinka, Insemination,
                                Fertilizers, Trainings, Ha_irrigated, Vaccination, FertilizerImprovedSeeds,)


class AgricultureListView(ListView):
    model = Crops
    template_name = "agriculture/agriculture_details.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AgricultureListView, self).get_context_data(**kwargs)
        context['crops'] = Crops.objects.all()
        context['seeds'] = Seeds.objects.all()
        context['ubwanikiro'] = Ubwanikiro.objects.all()
        context['terassis'] = UnusedTerassis.objects.all()
        context['bananas'] = Banana_and_Rehabilitation.objects.all()
        context['fertilizers'] = Fertilizers.objects.all()
        context['trainings'] = Trainings.objects.all()
        context['vaccinations'] = Vaccination.objects.all()
        context['imihigo'] = Umuhigo.objects.all()
        context['pumps'] = Pumps_in_Sector.objects.all()
        context['irrigation'] = Ha_irrigated.objects.all()
        context['inkazizakurikiranwa'] = InkaZizakurikiranwa.objects.all()
        context['girinka'] = Girinka.objects.all()
        context['inseminations'] = Insemination.objects.all()
        context['improved_seeds'] = FertilizerImprovedSeeds.objects.all()

        # view for crop, seeds, fertilizer, etc for each sector
        context['crop_sector'] = Crops.objects.filter(sector=self.request.user.user_profile.sector)
        context['seed_sector'] = Seeds.objects.filter(sector=self.request.user.user_profile.sector)
        context['ubwanikiro_sector'] = Ubwanikiro.objects.filter(sector=self.request.user.user_profile.sector)
        context['terrassis_sector'] = UnusedTerassis.objects.filter(sector=self.request.user.user_profile.sector)
        context['banana_sector'] = Banana_and_Rehabilitation.objects.filter(sector=self.request.user.user_profile.sector)
        context['improved_seed_sector'] = FertilizerImprovedSeeds.objects.filter(sector=self.request.user.user_profile.sector)
        context['insemination_sector'] = Insemination.objects.filter(sector=self.request.user.user_profile.sector)
        context['inkazizakurikiranwa_sector'] = InkaZizakurikiranwa.objects.filter(sector=self.request.user.user_profile.sector)
        context['girinka_sector'] = Girinka.objects.filter(sector=self.request.user.user_profile.sector)
        context['training_sector'] = Trainings.objects.filter(sector=self.request.user.user_profile.sector)
        context['fertilizer_sector'] = Fertilizers.objects.filter(sector=self.request.user.user_profile.sector)
        context['vaccination_sector'] = Vaccination.objects.filter(sector=self.request.user.user_profile.sector)
        context['irrigation_sector'] = Ha_irrigated.objects.filter(sector=self.request.user.user_profile.sector)
        context['number_of_pump_sector'] = Pumps_in_Sector.objects.filter(sector=self.request.user.user_profile.sector)
        context['imihigo_sector'] = Umuhigo.objects.filter(sector=self.request.user.user_profile.sector)

        return context
