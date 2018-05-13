# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-10 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ram', '0003_employeedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedata',
            name='emp_id',
            field=models.CharField(blank=True, db_column='EMP_ID', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employeedata',
            name='emp_mobile',
            field=models.CharField(blank=True, db_column='EMP_MOBILE', max_length=10, null=True),
        ),
    ]
