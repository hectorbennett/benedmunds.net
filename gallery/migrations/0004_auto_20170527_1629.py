# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-27 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20170527_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='image',
            field=models.ImageField(upload_to='artwork/%Y/%m/'),
        ),
    ]
