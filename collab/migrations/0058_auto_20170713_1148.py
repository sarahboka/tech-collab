# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 11:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0057_auto_20170713_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 13, 11, 48, 33, 467000), verbose_name='Date'),
        ),
    ]
