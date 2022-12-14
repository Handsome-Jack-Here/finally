# Generated by Django 4.1.2 on 2022-10-26 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0036_band_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='track',
            name='single',
            field=models.BooleanField(default=False),
        ),
    ]
