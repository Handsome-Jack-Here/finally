# Generated by Django 4.1.1 on 2022-10-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0022_remove_commentdb_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='comments',
            field=models.ManyToManyField(related_name='Albums', to='music_app.commentdb'),
        ),
    ]
