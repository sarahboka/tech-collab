# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20170708_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='message',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
