from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, TemplateView, FormView, CreateView
from django.views import View
from .models import Band, Album, Track, CommentDB, Genre
from .forms import CommentAbout
from random import sample


class BandsList(ListView):
    template_name = 'music_app/index.html'
    model = Band

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['genres'] = Genre.objects.all()
        random = []
        for i in Genre.objects.all():
            random.append(i)
        random = sample(random, 14)
        context['genres'] = random
        return context

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

    def get_context_data(self, **kwargs):
        context = super(TrackDetail, self).get_context_data(**kwargs)
        length = Track.objects.get(slug=self.kwargs['slug'])
        str_length = str(length.length)
        context['length'] = (str_length[0] + ':' + str_length[2:])
        return context


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


class GenresList(ListView):
    model = Genre
    template_name = 'music_app/genres_list.html'
    context_object_name = 'genres'


class GenreDetail(DetailView):
    model = Genre
    template_name = 'music_app/genre_detail.html'
    context_object_name = 'genre'
