# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 15:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0048_auto_20170711_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 11, 15, 1, 53, 880000), verbose_name='Date'),
        ),
    ]
