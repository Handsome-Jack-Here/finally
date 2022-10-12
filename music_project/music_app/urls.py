from django.urls import path
from . import views

urlpatterns = [
    path('', views.BandsList.as_view()),
    path('band/<slug:slug>/', views.BandDetail.as_view(), name='get-band-detail'),
    path('album/<slug:slug>/', views.AlbumDetail.as_view(), name='get-album-detail'),
    path('track/<slug:slug>/', views.TrackDetail.as_view() , name='get-track-detail'),
]
