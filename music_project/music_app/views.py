from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView
from .models import Band, Album, Track
from .forms import CommentAbout


class BandsList(ListView):
    template_name = 'music_app/bands_list.html'
    model = Band
    context_object_name = 'bands'


class BandDetail(DetailView):
    template_name = 'music_app/band_detail.html'
    model = Band
    context_object_name = 'band'


class AlbumDetail(DetailView):
    template_name = 'music_app/album_detail.html'
    model = Album
    context_object_name = 'album'


class TrackDetail(DetailView):
    template_name = 'music_app/track_detail.html'
    model = Track
    context_object_name = 'track'


class AlbumCommentForm(CreateView):
    template_name = 'music_app/comment_form.html'
    form_class = CommentAbout
    context_object_name = ['form', ]
    success_url = '/'
