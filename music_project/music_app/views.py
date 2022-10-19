from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView
from django.views import View
from .models import Band, Album, Track, CommentDB
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
    def get_context_data(self, **kwargs):
        context = super(AlbumCommentForm, self).get_context_data(**kwargs)
        context['default'] = self.kwargs['pk']
        return context

    template_name = 'music_app/comment_form.html'
    form_class = CommentAbout
    model = CommentDB
    context_object_name = 'form'
    success_url = '/'


