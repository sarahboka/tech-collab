# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 00:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0016_auto_20170707_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 8, 0, 25, 59, 478000, tzinfo=utc), verbose_name='Date'),
        ),
    ]