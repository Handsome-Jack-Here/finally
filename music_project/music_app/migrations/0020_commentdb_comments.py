# Generated by Django 4.1.1 on 2022-10-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0019_commentdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentdb',
            name='comments',
            field=models.ManyToManyField(related_name='comments', to='music_app.album'),
        ),
    ]
