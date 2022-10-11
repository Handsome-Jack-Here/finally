from django.db import models
from django.urls import reverse


class Album(models.Model):
    title = models.CharField(max_length=40)
    release_date = models.DateField()


class Band(models.Model):
    GENRES = [
        ('NO GENRE', 'No genre'),
        ('INDUSTRIAL', 'Industrial'),
        ('ROCK', 'Rock'),
        ('JAZZ', 'Jazz'),
        ('ELECTRONIC', 'Electronic'),
        ('DISCO', 'Disco'),
        ('R&B', 'Rhythm and Blues'),
        ('COUNTRY', 'Country'),
        ('POP', 'Pop'),
        ('NEW AGE', 'New age'),
        ('METAL', 'Metal')
    ]

    band_name = models.CharField(max_length=40, blank=False)
    founded = models.IntegerField(blank=False)
    genre = models.CharField(choices=GENRES, blank=False, default='No genre', max_length=14)
    country = models.CharField(max_length=40, blank=True)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f'{self.band_name} {self.genre} {self.founded}'
