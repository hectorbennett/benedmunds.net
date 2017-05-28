# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-28 14:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_auto_20170528_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='medium',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artwork',
            name='date_created',
            field=models.DateField(),
        ),
    ]