# Generated by Django 4.1.1 on 2022-10-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0016_track'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.TextField(default='No description', max_length=1500),
        ),
    ]
