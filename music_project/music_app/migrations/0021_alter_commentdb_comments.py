# Generated by Django 4.1.1 on 2022-10-13 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0020_commentdb_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentdb',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='comments', to='music_app.album'),
        ),
    ]
