# Generated by Django 4.1.1 on 2022-10-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0017_band_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='description',
            field=models.TextField(default='No description', max_length=2500),
        ),
    ]