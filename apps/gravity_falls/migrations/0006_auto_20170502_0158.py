# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 06:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gravity_falls', '0005_auto_20170502_0157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_time',
            field=models.TimeField(),
        ),
    ]
