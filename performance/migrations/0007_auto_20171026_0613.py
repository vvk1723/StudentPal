# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 00:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('performance', '0006_course_exam'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='sem',
            new_name='user',
        ),
    ]
