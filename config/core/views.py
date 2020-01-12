from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Movie,Personal

class MoviesReview(ListView):
    model=Movie
    

class DetailView(DetailView):
    model=Movie

def handler404(request):
    return render(request, '404.html')

class PersonalView(DetailView):
    model=Personal