# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_auto_20170110_1832'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenarios',
            name='name',
            field=models.CharField(default=b'2017-01-10 18:38:18.557928+00:00', max_length=512),
        ),
    ]
