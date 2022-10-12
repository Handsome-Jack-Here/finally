from django.urls import path
from . import views

urlpatterns = [
    path('', views.BandsList.as_view()),
    path('band/<slug:slug>/', views.BandDetail.as_view(), name='get-band-detail'),
]
