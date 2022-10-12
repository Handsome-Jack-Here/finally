# Generated by Django 4.1.1 on 2022-10-12 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0015_delete_track_rename_group_album_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('length', models.FloatField(default=1.0)),
                ('slug', models.SlugField(blank=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tracks', to='music_app.album')),
            ],
        ),
    ]
