# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-07 11:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ram', '0002_conditions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conditions',
            name='desc_conditions',
        ),
    ]