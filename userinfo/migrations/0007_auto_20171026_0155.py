# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0006_profile_current_sem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('N', 'I prefer not to say')], default='', max_length=1),
        ),
    ]
