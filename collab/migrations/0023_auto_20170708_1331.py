# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 13:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0022_auto_20170708_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 8, 13, 31, 21, 701000), verbose_name='Date'),
        ),
    ]
