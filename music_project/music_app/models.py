from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MinLengthValidator, MaxValueValidator
from django.utils.text import slugify


class Genre(models.Model):
    title = models.CharField(max_length=38)
    slug = models.SlugField(blank=True)

    def __str__(self):
        return f'{self.title}'

    def get_url(self):
        return reverse('get-genre', args=[self.slug, ])


class Band(models.Model):
    image = models.FileField(upload_to='img', blank=True)
    band_name = models.CharField(max_length=40, blank=False)
    founded = models.IntegerField(blank=False)
    country = models.CharField(max_length=40, blank=True)
    description = models.TextField(max_length=2500, default='No description')
    slug = models.SlugField(blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=5)

    genres = models.ManyToManyField(Genre, related_name='bands')

    def __str__(self):
        return f'{self.band_name}'

    def get_url(self):
        return reverse('get-band-detail', args=[self.slug, ])


class Album(models.Model):
    title = models.CharField(max_length=40)
    release_date = models.DateField()
    slug = models.SlugField(blank=True)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=5)

    genres = models.ManyToManyField(Genre, related_name='albums')
    band = models.ForeignKey(Band, on_delete=models.PROTECT, null=True, related_name='albums')

    def __str__(self):
        return f'{self.title}'

    def get_url(self):
        return reverse('get-album-detail', args=[slugify(self.band), self.slug])

    def get_form(self):
        return reverse('make-a-comment', args=[self.slug, self.pk])


class Track(models.Model):
    title = models.CharField(max_length=40)
    length = models.FloatField(default=1.00)
    slug = models.SlugField(blank=True)
    single = models.BooleanField(default=False)

    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='tracks', null=True)
    album = models.ForeignKey(Album, on_delete=models.PROTECT, related_name='tracks')

    def __str__(self):
        return f'{self.title}'

    def get_url(self):
        # album = self.album
        album = Album.objects.get(title=self.album)
        band = album.band
        return reverse('get-track-detail', args=[slugify(band), slugify(album), self.slug, ])


class CommentDB(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(2)])
    surname = models.CharField(max_length=40, validators=[MinLengthValidator(2)])
    comment = models.TextField(max_length=1500, validators=[MinLengthValidator(10)])
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    album = models.ForeignKey(Album, on_delete=models.PROTECT, blank=True, null=True, related_name='comments', )

    def __str__(self):
        return f'{self.name} {self.surname} {self.comment}'
