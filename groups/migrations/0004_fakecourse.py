# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 20:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_invite_is_requested'),
    ]

    operations = [
        migrations.CreateModel(
            name='FakeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.CustomGroup')),
            ],
        ),
    ]
