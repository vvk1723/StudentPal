# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 23:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0005_auto_20171009_0308'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='current_sem',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]