# Generated by Django 4.1.1 on 2022-10-11 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0005_rename_release_album_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='country',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
