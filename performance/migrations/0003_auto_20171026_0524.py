# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 23:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0002_auto_20171026_0517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='sem',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Exam',
        ),
    ]
