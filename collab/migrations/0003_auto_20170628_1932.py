# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 23:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0002_auto_20170628_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 28, 19, 32, 18, 148000), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='technology',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
