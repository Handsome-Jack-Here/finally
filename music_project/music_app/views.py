from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView
from .models import Band


class BandsList(ListView):
    template_name = 'music_app/bands_list.html'
    model = Band
    context_object_name = 'bands'


class BandDetail(DetailView):
    template_name = 'music_app/band_detail.html'
    model = Band
    context_object_name = 'band'