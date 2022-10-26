from django.contrib import admin
from .models import Band, Album, Track, CommentDB, Genre


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['band_name', 'founded', 'description', 'slug', ]
    prepopulated_fields = {'slug': ('band_name',)}


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ['title', 'release_date', 'band', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', ]
    prepopulated_fields = {'slug': ('title',)}


@admin.register(CommentDB)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ['name', 'surname', 'comment', 'rating', ]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_filter = ['title', ]
    prepopulated_fields = {'slug':('title', )}

