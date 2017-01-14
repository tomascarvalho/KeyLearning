# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 15:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('game', '0016_auto_20170111_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge_type', models.CharField(choices=[('1', 'Points'), ('2', 'Scenario')], max_length=2)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='scenarios',
            name='name',
            field=models.CharField(default=b'2017-01-12 15:05:33.902789+00:00', max_length=512),
        ),
        migrations.AddField(
            model_name='badge',
            name='scenario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Scenarios'),
        ),
        migrations.AddField(
            model_name='badge',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
