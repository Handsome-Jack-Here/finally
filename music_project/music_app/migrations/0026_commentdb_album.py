# Generated by Django 4.1.1 on 2022-10-13 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0025_remove_album_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentdb',
            name='album',
            field=models.ManyToManyField(related_name='comments', to='music_app.album'),
        ),
    ]