# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_scenarios_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenarios',
            name='name',
            field=models.CharField(default=b'2017-01-11 14:07:24.609264+00:00', max_length=512),
        ),
        migrations.AlterField(
            model_name='scenarios',
            name='notes',
            field=models.TextField(),
        ),
    ]
