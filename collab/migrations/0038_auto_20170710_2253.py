# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 22:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('collab', '0037_auto_20170710_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 10, 22, 53, 17, 53000), verbose_name='Date'),
        ),
    ]
