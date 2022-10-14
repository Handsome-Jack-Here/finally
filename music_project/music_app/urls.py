from django.urls import path
from . import views

urlpatterns = [
    path('', views.BandsList.as_view()),
    path('<slug:slug>/', views.BandDetail.as_view(), name='get-band-detail'),
    path('<str:title>/<slug:slug>/', views.AlbumDetail.as_view(), name='get-album-detail'),
    path('<str:bend>/<str:album>/<slug:slug>', views.TrackDetail.as_view(), name='get-track-detail'),

    path('comment_for/<slug:slug>', views.AlbumCommentForm.as_view(), name='make-a-comment'),
]
