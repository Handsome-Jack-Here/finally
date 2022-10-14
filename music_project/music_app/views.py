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


class AlbumCommentForm(FormView):
    def get_context_data(self, **kwargs):
        context = super(AlbumCommentForm, self).get_context_data(**kwargs)
        print(self.kwargs['slug'])
        context['fuck'] = self.kwargs['slug']
        return context

    model = CommentDB
    template_name = 'music_app/comment_form.html'
    form_class = CommentAbout
    context_object_name = 'form'
    success_url = '/'

# make a routh for success contain write function form to Album.x.comments

# class FeedbackViewUpdate(View):
#     def get(self, request, id_feedback):
#         current_feedback = FeedbackDB.objects.get(id=id_feedback)
#         form = FeedbackForm(instance=current_feedback)
#         return render(request, 'form_app/form.html', context={'form': form})
#
#     def post(self, request, id_feedback):
#         current_feedback = FeedbackDB.objects.get(id=id_feedback)
#         form = FeedbackForm(request.POST, instance=current_feedback)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(f'/{id_feedback + 1}')  # /'done'
