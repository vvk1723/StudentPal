# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customgroup',
            name='description',
            field=models.TextField(default=''),
        ),
    ]