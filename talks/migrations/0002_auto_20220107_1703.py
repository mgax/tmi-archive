# Generated by Django 3.2.5 on 2022-01-07 17:03

import django.core.validators
from django.db import migrations, models
import dynamic_filenames
import taggit.managers
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('talks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='audio_cleaned',
            field=models.FileField(blank=True, null=True, upload_to=dynamic_filenames.FilePattern(filename_pattern='audio/cleaned/tmi-archive-{uuid:.12base32}.mp3'), validators=[django.core.validators.FileExtensionValidator(['mp3'])]),
        ),
        migrations.AlterField(
            model_name='talk',
            name='audio_original',
            field=models.FileField(blank=True, null=True, upload_to=dynamic_filenames.FilePattern(filename_pattern='audio/original/tmi-archive-{uuid:.12base32}.mp3'), validators=[django.core.validators.FileExtensionValidator(['mp3'])]),
        ),
        migrations.AlterField(
            model_name='talk',
            name='description',
            field=tinymce.models.HTMLField(null=True),
        ),
    ]
