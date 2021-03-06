# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 00:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0006_auto_20170630_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 20, 49, 36, 130000), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='technologies',
            field=models.ManyToManyField(blank=True, to='collab.Technology'),
        ),
    ]
