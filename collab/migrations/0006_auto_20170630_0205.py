# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 06:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0005_auto_20170629_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 30, 2, 5, 26, 836000), verbose_name='Date'),
        ),
    ]
