# Generated by Django 4.1.1 on 2022-10-19 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0033_remove_band_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='genres',
            field=models.ManyToManyField(related_name='bands', to='music_app.genre'),
        ),
    ]
