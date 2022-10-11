from django.contrib import admin
from .models import Band


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['band_name', 'founded', 'genre', 'slug']
    prepopulated_fields = {'slug': ('band_name',)}
