# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-29 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_auto_20170723_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='total_hours_worked',
            field=models.IntegerField(default=0),
        ),
    ]