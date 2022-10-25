# Generated by Django 4.1.1 on 2022-10-19 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0034_alter_band_genres'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='genres',
            field=models.ManyToManyField(related_name='albums', to='music_app.genre'),
        ),
        migrations.AddField(
            model_name='track',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='music_app.genre'),
        ),
    ]
