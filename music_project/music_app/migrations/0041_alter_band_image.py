# Generated by Django 4.1.2 on 2022-11-06 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0040_alter_band_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.FileField(blank=True, default=None, null=True, upload_to='img'),
        ),
    ]
