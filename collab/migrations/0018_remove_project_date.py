# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 00:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collab', '0017_auto_20170707_2025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date',
        ),
    ]