from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView


class HomePageView(TemplateView):
    template_name = "pages/index.html"
    



