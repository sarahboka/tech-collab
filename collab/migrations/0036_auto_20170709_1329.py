# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 13:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0035_auto_20170709_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 9, 13, 29, 7, 919000), verbose_name='Date'),
        ),
    ]
