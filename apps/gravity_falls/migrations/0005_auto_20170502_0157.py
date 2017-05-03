# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gravity_falls', '0004_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='usertasks', to='login_app.User'),
        ),
    ]
