# Generated by Django 4.1.1 on 2022-10-13 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0021_alter_commentdb_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentdb',
            name='comments',
        ),
    ]
