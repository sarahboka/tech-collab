# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 00:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0032_auto_20170708_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 9, 0, 12, 30, 344000), verbose_name='Date'),
        ),
    ]
