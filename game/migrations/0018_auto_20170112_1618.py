# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 16:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0017_auto_20170112_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='badge',
            name='badge_type',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='scenarios',
            name='name',
            field=models.CharField(default=b'2017-01-12 16:18:00.310529+00:00', max_length=512),
        ),
    ]
