# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-21 11:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0008_auto_20170717_2347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maintenance',
            name='maintenance_date',
        ),
        migrations.AddField(
            model_name='maintenance',
            name='end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maintenance',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
