# Generated by Django 4.0.1 on 2022-01-20 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0005_alter_playlist_first_recording_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='transcription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='talk',
            name='transcription_deepgram',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='first_recording_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
