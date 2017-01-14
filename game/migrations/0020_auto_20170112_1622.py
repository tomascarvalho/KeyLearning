# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 16:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0019_auto_20170112_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='badge',
        ),
        migrations.AddField(
            model_name='badge',
            name='badge_type',
            field=models.CharField(choices=[('1', 'Points'), ('2', 'Scenario')], default='1', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scenarios',
            name='name',
            field=models.CharField(default=b'2017-01-12 16:22:37.514406+00:00', max_length=512),
        ),
    ]
