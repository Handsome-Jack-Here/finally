# Generated by Django 4.1.1 on 2022-10-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0010_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='tracks',
            field=models.ManyToManyField(related_name='tracks', to='music_app.track'),
        ),
    ]
